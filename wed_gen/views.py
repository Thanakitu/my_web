from django.http import HttpRequest
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'wed_gen/home.html')

def about(request):
    return render(request, 'wed_gen/about.html')

def change_theme(request: HttpRequest):
    referer = request.headers.get("referer")
    if referer is not None:
        response = HttpResponseRedirect(referer)
    else:
        response = HttpResponseRedirect(reverse("home"))

    # Theme
    theme = request.GET.get("theme")
    if theme == "dark":
        expired_date = datetime.now() + timedelta(days=365)
        response.set_cookie("theme", "dark", expires=expired_date, samesite="Lax")
    else:
        response.delete_cookie("theme")

    return response