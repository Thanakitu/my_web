from django.contrib import admin
from wed_res.models import Res

# Register your models here.
class ResAdmin(admin.ModelAdmin):
    list_display = ['title','date','phone']
    search_fields = ['title',]

admin.site.register(Res,ResAdmin)