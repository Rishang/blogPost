from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.urls import reverse
from django.http import HttpResponseRedirect

class CreateUser(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100,min_length=2)
    last_name = forms.CharField(max_length=100,min_length=2)
    
    class Meta:    
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')


class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100,min_length=2)
    last_name = forms.CharField(max_length=100,min_length=2)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'image',
            'about',
            "social_insta",
            "social_facebook",
            "social_twitter"
        )
    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('user_profile'))
