from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
