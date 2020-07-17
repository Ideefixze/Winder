from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileSettingsForm(ModelForm):
    #first_name = forms.CharField(label='First name', max_length=50, required=False)
    #last_name = forms.CharField(label='Last name', max_length=50, required=False)
    #profile_picture = forms.ImageField(label='Profile Picture', required=False)
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')