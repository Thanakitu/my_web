from django.contrib import admin
from wed_hotel.models import Hotel

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['title','number','star']
    search_fields = ['title','number',]

admin.site.register(Hotel,HotelAdmin)