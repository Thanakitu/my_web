from django.urls import path
from wed_hotel import views

urlpatterns = [
    path('', views.hotels, name='hotels'),
    path('<int:hotel_id>',views.hotel, name='hotel'),
]