# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Class with user register form
    Form for auth new teacher
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    Class with update form
    You can change email and username
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Class with update profile info, update profile image
    """
    class Meta:
        model = Profile
        fields = ['image']
