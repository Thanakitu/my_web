from django.db import models
# Create your models here.

class Location(models.Model):
    title = models.CharField(max_length=60)
    is_Recommend = models.BooleanField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)  
    googlemap = models.URLField(max_length=500, blank=True)
    at_location = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    image_a = models.CharField(max_length=50, null=True, blank=True)
    image_b = models.CharField(max_length=50, null=True, blank=True)