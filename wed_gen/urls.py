from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path("change_theme", views.change_theme, name="change_theme"),
]
