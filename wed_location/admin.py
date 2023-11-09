from django.contrib import admin
from wed_location.models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title','is_Recommend','date']
    search_fields = ['title']

admin.site.register(Location,LocationAdmin)