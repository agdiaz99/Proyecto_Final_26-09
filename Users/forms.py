from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Nombre de usuario', max_length=20)
    email=forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    username=forms.CharField(label='Nombre de usuario')
    email=forms.EmailField(label='Dirección e-mail')
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Seleccione una imagen")