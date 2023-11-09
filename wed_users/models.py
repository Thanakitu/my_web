from django.contrib.auth.models import AbstractUser
from django.db import models

#Create your models here.

class CustomUser(AbstractUser):
   email = models.EmailField(unique=True)
   favorite_location_set = models.ManyToManyField(
      to="wed_location.Location",
      through="wed_users.UserFavoriteLocation",
      related_name="favorited_user_set",
   )
    
class Profile(models.Model):
   phone = models.CharField(max_length=15, default="", blank=True)
   user = models.OneToOneField("wed_users.CustomUser", on_delete=models.CASCADE)
    
class UserFavoriteLocation(models.Model):
   LEVELS = [(1, "⭐"), (2, "⭐⭐"), (3, "⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (5, "⭐⭐⭐⭐⭐")]
    
   level = models.SmallIntegerField(choices=LEVELS, default=1)
   user = models.ForeignKey(
      "wed_users.CustomUser",
      on_delete=models.CASCADE,
      related_name="favorite_location_pivot_set",
   )
   location = models.ForeignKey(
      "wed_location.Location",
      on_delete=models.CASCADE,
      related_name="favorited_user_pivot_set",
   )
   
   class Meta:
        constraints = [
            models.UniqueConstraint(fields=("user", "location"), name="unique_user_location")
        ]

   def level_label(self) -> str:
        selected_level = [l for l in self.LEVELS if l[0] == self.level][0]
        return selected_level[1]