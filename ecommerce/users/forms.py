from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Username: ')
    email = forms.EmailField(max_length=200, label='Email: ')
    first_name = forms.CharField(max_length=150, label='First Name: ')
    last_name = forms.CharField(max_length=150, label='Last Name: ')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
