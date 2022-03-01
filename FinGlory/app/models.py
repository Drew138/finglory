from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Gastos(models.TextChoices):
    class TipoRecurrencia(models.Model):
        mensual = 'Mensual'
        anual = 'Anual'
        no_recurrente = 'No recurrente'
        
    class  CategoriaGastos(models.TextChoices):
        alimentacion = 'Alimentación'
        hogar = 'Hogar'
        entretenimiento = 'Entretenimiento'
        educacion = 'Educación'
        compromisos_bancarios = 'Compromisos Bancarios'
        otros = 'Otros'
    categoria = models.CharField(max_length=30, choices = CategoriaGastos.choices, default = CategoriaGastos.otros )
    recurrencia = models.charField(max_length=20, choices = TipoRecurrencia.choices, default = TipoRecurrencia.Mensual)
    nombre = models.CharField(max_length=30, null=False)
    fecha = models.DateTimeField(null=False, blank=True)
    cantidad = models.IntegerField(default=0, blank=True, null=False)
    factura = models.ImageField(upload_to = 'images')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Ingresos(models.TextChoices):
    class TipoRecurrencia(models.Model):
        mensual = 'Mensual'
        anual = 'Anual'
        no_recurrente = 'No recurrente'

    recurrencia = models.charField(max_length=20, choices = TipoRecurrencia.choices, default = TipoRecurrencia.Mensual)
    nombre = models.CharField(max_length=30, null=False)
    fecha = models.DateTimeField(null=False, blank=True) 
    cantidad = models.IntegerField(default=0, blank=True, null=False)

