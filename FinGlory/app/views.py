from django.shortcuts import render
from django.http import HttpResponse

#create your views here

def home(request):
    return render(request, 'home.html')


def eliminar_ingresos(request):
    return render(request, 'eliminar_ingresos/eliminar_ingreso.html')

def eliminar_gastos(request):
    return render(request, 'paginas/gastos.html')
