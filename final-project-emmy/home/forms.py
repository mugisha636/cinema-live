
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    names = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['names', 'username', 'email', 'password1', 'password2']

# here we are formating the register form the way want it to be
