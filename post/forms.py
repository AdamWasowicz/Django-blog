from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, required=True,label="Password")
    
    class Meta:
        model = User
        exclude = ['hashed_password', 'register_date']
        labels = {
            'username': "Your username",
            'email': "Your email"
        }