from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'form-control',
    # }))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'class':'form-control',
    #      'placeholder':"name@example.com"
    # }))
    # message = forms.CharField(widget=forms.Textarea(attrs={
    #     'class':'form-control',
    #     'rows':"3"
    # }))
    
    class Meta:
        model = Contact
        # fields = ['name','email','message']
        fields = '__all__'
        # exclude = ('email',)

# class ContactForm(forms.Form):
#     name  = forms.CharField(max_length=150)
#     email  = forms.EmailField()
#     message = forms.CharField(max_length=150)

