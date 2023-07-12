from django import forms
from store.models import *

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'