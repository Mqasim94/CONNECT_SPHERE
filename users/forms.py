from django.contrib.auth .forms import UserCreationForm
from django.core import validators
from .models import User
from django import forms

class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       

      

    def __init__(self, *args, **kwargs):
        super(Register_Form, self).__init__(*args, **kwargs)
        
       
        self.fields['username'].error_messages = {
            'required': 'This field is required.',
            'unique': 'This username is already taken. Please choose a different one.',
            'invalid': 'Enter a valid username.'
        }

        self.fields['email'].error_messages = {
            'required': 'This field is required.',
            'unique': 'This email address is already registered. Please use a different one.',
            'invalid': 'Enter a valid email address.',
            'invalid_at_sign': 'Email must contain the "@" sign.',
        }

        self.fields['password1'].error_messages = {
            'required': 'This field is required.',
            'min_length': 'Password must be at least 8 characters long.',
            'password_mismatch': 'The two password fields didnt match.'
        }

        self.fields['password2'].error_messages = {
            'required': 'This field is required.',
            'password_mismatch': 'The two password fields didnt match.'
        }


class Signin_Form(forms.Form):
    username = forms.CharField( max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)