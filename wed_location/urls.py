from django.urls import path
from wed_location import views

urlpatterns = [
    path('', views.locations, name='locations'),
    path('<int:location_id>',views.location, name='location'),
    path("<int:location_id>/favorite", views.favorite_location, name="favorite_location"),
    path("<int:location_id>/unfavorite", views.unfavorite_location, name="unfavorite_location"),
]
