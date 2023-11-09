from django.db import models
# Create your models here.

class Hotel(models.Model):
    title = models.CharField(max_length=60) 
    number = models.CharField(max_length=5, blank=True) 
    at_location = models.CharField(max_length=100, blank=True)
    googlemap = models.URLField(max_length=500, blank=True)
    agoda = models.URLField(max_length=500, blank=True)
    image_agoda = models.CharField(max_length=50, null=True, blank=True)
    tra = models.URLField(max_length=700, blank=True)
    image_tra = models.CharField(max_length=50, null=True, blank=True)
    star = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=50, null=True, blank=True)