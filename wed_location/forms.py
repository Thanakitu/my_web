from django import forms
from wed_users.models import UserFavoriteLocation


class FavoriteLocationForm(forms.ModelForm):
    class Meta:
        model = UserFavoriteLocation
        fields = ["level"]
        widgets = {"level": forms.RadioSelect}
