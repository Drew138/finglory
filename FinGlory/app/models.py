from django.urls import translate_url
from .choices import *
from djongo import models

# Create your models here.

class Usuario(models.Model):
    Id = models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=254, null=False)
    contraseña = models.CharField(max_length=20, null=False)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=False)

class Gastos(models.Model):
    gastos_id = models.AutoField(primary_key=True, null=False)
    nombre_gasto = models.CharField(max_length=30, null=False)
    fecha = models.DateTimeField(null=False, blank=True)
    cantidad = models.IntegerField(default=0, blank=True, null=False)
    recurrencia = models.CharField(max_length=30, choices= TipoRecurrencia.choices, null=False, blank=False)
    categoria = models.CharField(max_length=255, choices=CategoriaGastos.choices, null=False, blank=False)
    factura = models.ImageField(upload_to = 'app/images/', null=translate_url)

class Ingresos(models.Model):
    ingreso_id = models.AutoField(primary_key=True, null=False) 
    nombre_ingresos = models.CharField(max_length=30, null=False)
    fecha = models.DateTimeField(null=False, blank=True) 
    cantidad = models.IntegerField(default=0, blank=True, null=False)
    recurrencia = models.CharField(max_length=30, choices= TipoRecurrencia.choices, null=False, blank=False)
