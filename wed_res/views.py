from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
import re

from wed_res.models import Res
from wed_location.forms import FavoriteLocationForm
from wed_users.models import UserFavoriteLocation

def ress(request):
    all_ress = Res.objects.order_by('-at_location')
    context = { 'ress': all_ress }
    return render(request, 'wed_res/ress.html',context)

def res(request:HttpRequest, res_id):
    one_res = None
    is_favorite_res = False
    try:
        one_res = Res.objects.get(id=res_id)
        if request.user.is_authenticated:
            user_favorite_res = UserFavoriteLocation.objects.get(
                    user=request.user, res=one_res
            )
            is_favorite_res = user_favorite_res is not None
    except:
        print("หาไม่เจอ")
                
    form = FavoriteLocationForm()
    context = {'res': one_res, "form": form, "is_favorite_hotel": is_favorite_res}
    return render(request, 'wed_res/res.html', context)
