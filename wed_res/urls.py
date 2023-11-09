from django.urls import path
from wed_res import views

urlpatterns = [
    path('', views.ress, name='ress'),
    path('<int:res_id>',views.res, name='res'),
]