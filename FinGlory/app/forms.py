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
            'categoria': '¿Qué tipo de gasto es?',
            'recurrencia': '¿Cada cuánto?',
            'nombre': '¿Qué gasto es?',
            'fecha': '¿Cuándo fue?',
            'cantidad': '¿Cuánto gastaste?',
            'factura': 'Adjunte su factura'
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
            'recurrencia': '¿Cada cuánto?',
            'nombre': '¿Qué ingreso es?',
            'fecha': '¿Cuándo fue?',
            'cantidad': '¿Cuánto ganaste?',
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