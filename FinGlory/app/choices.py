from xml.parsers.expat import model
from django.db import models

class CategoriaGastos(models.TextChoices):
    alimentación = 'alimentación'
    hogar = 'hogar'
    entretenimiento = 'entretenimiento'
    educación = 'educación'
    Compromisos_Bancarios = 'Compromisos Bancarios'
    Otros = 'Otros'

class TipoRecurrencia(models.TextChoices):
    mensual = 'mensual'
    anual = 'anual'
    no_recurrente = 'no_recurrente'