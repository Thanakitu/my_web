from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
import re

from wed_location.models import Location
from wed_location.forms import FavoriteLocationForm
from wed_users.models import UserFavoriteLocation

def locations(request):
    all_locations = Location.objects.order_by('-is_Recommend')
    context = { 'locations': all_locations }
    return render(request, 'wed_location/locations.html',context)

def location(request:HttpRequest, location_id):
    one_location = None
    is_favorite_location = False
    try:
        one_location = Location.objects.get(id=location_id)
        if request.user.is_authenticated:
            user_favorite_location = UserFavoriteLocation.objects.get(
                    user=request.user, location=one_location
            )
            is_favorite_location = user_favorite_location is not None
    except:
        print("หาไม่เจอ")
                
    form = FavoriteLocationForm()
    context = {'location': one_location, "form": form, "is_favorite_location": is_favorite_location}
    return render(request, 'wed_location/location.html', context)


@login_required
def favorite_location(request: HttpRequest, location_id):
    if request.method == "POST":
        form = FavoriteLocationForm(request.POST)
        if form.is_valid():
            obj, is_created = UserFavoriteLocation.objects.update_or_create(
                user=request.user,
                location=Location(id=location_id),
                defaults={"level": form.cleaned_data.get("level")},
            )
            print("Create favorite" if is_created else "Update favorite")

    return HttpResponseRedirect(reverse("location", args=[location_id]))


@login_required
def unfavorite_location(request: HttpRequest, location_id):
    if request.method == "POST":
        request.user.favorite_location_set.remove(Location(id=location_id))
    return HttpResponseRedirect(reverse("dashboard"))

def is_valid_url(url):
    url_pattern = re.compile(r'^https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$')
    return re.match(url_pattern, url) is not None