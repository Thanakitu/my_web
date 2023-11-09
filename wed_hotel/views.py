from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
import re

from wed_hotel.models import Hotel
from wed_location.forms import FavoriteLocationForm
from wed_users.models import UserFavoriteLocation

def hotels(request):
    all_hotels = Hotel.objects.order_by('number')
    context = { 'hotels': all_hotels }
    return render(request, 'wed_hotel/hotels.html',context)

def hotel(request:HttpRequest, hotel_id):
    one_hotel = None
    is_favorite_hotel = False
    try:
        one_hotel = Hotel.objects.get(id=hotel_id)
        if request.user.is_authenticated:
            user_favorite_hotel = UserFavoriteLocation.objects.get(
                    user=request.user, hotel=one_hotel
            )
            is_favorite_hotel = user_favorite_hotel is not None
    except:
        print("หาไม่เจอ")
                
    form = FavoriteLocationForm()
    context = {'hotel': one_hotel, "form": form, "is_favorite_hotel": is_favorite_hotel}
    return render(request, 'wed_hotel/hotel.html', context)
