from django.db import models
# Create your models here.

class Res(models.Model):
    title = models.CharField(max_length=60) 
    at_location = models.CharField(max_length=200, blank=True)
    googlemap = models.URLField(max_length=500, blank=True)
    date = models.CharField(max_length=100, blank=True) 
    phone = models.CharField(max_length=50, blank=True)
    wed = models.URLField(max_length=500, blank=True)
    image = models.CharField(max_length=50, null=True, blank=True)