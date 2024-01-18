from django.contrib.auth .forms import UserCreationForm
from .models import User
from django import forms

class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Signin_Form(forms.Form):
    username = forms.CharField(max_length= 128)
    password = forms.CharField(widget=forms.PasswordInput)