from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

def gastos(request):
    gasto = Gastos.objects.all()
    context = {'gastos': gasto}
    return render(request, 'gastos.html', context)

def ingresos(request):
    ingreso = Ingresos.objects.all()
    context = {'ingresos': ingreso}
    return render(request, 'ingresos.html', context)

def registrarGastosView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Gastos, id=pk)
        if request.method == 'POST':
            form = RegistrarGastosForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = RegistrarGastosForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/gastos/') #Pendiente a revisar
                else:
                    messages.error(request, form.errors)
        else:
            form = RegistrarGastosForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = RegistrarGastosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/gastos/') #Pendiente a revisar
            else:
                messages.error(request, form.errors)
    else: 
        form =  RegistrarGastosForm()

    return render(request, 'gastos.html', {'form': form} )



def registrarIngresosView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Ingresos, id=pk)
        if request.method == 'POST':
            form = RegistrarIngresosForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = RegistrarIngresosForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/ingresos/') #Pendiente a revisar
                else:
                    messages.error(request, form.errors)
        else:
            form = RegistrarIngresosForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = RegistrarIngresosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/ingresos/') #Pendiente a revisar
            else:
                messages.error(request, form.errors)
    else: 
        form =  RegistrarIngresosForm()    
    
    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'form.html', context)
    