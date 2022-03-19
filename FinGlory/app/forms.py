from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django import forms
from matplotlib import widgets
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class RegistrarGastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = [
            'categoria',
            'recurrencia',
            'nombre',
            'fecha',
            'cantidad',
            'factura'
        ]
        labels = {
            'categoria': '¿Que tipo de gastos es?',
            'recurrencia': '¿Cada cuanto?',
            'nombre': '¿Que gasto es?',
            'fecha': '¿Cundo fue?',
            'cantidad': '¿Cuanto gastaste?',
            'factura': 'Adjunta tu factura'
        }
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'recurrencia': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'factura': forms.FileInput(attrs={'class': 'form-control'}),
        }


class RegistrarIngresosForm(forms.ModelForm):
    class Meta:
        model = Ingresos
        fields = [
            'recurrencia',
            'nombre',
            'fecha',
            'cantidad'
        ]
        labels = {
            'recurrencia': '¿Cada cuanto?',
            'nombre': '¿Que ingreso es?',
            'fecha': '¿Cundo fue?',
            'cantidad': '¿Cuanto ganaste?',
        }
        widgets = {
            'recurrencia': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']