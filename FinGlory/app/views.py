
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


#create your views here

def home(request):
    return render(request, 'home.html')


def inicio(request):
    return render(request, 'inicio.html')


def gastos(request):
    gasto = Gastos.objects.all()
    context = {'gastos': gasto}
    return render(request, 'gastos.html', context)


def ingresos(request):
    ingreso = Ingresos.objects.all()
    context = {'ingresos': ingreso}
    return render(request, 'ingresos.html', context)

    if request.method == 'POST':
        pass



def registrarGastosView(request, *args, **kwargs):
    if request.method == 'POST':
        if 'crear' in request.POST:
            form = RegistrarGastosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/gastos/')  # Pendiente a revisar
            else:
                messages.error(request, form.errors)
    else:
        form = RegistrarGastosForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None), 'nombre_modelo': 'Gasto'}

    return render(request, 'form.html', context)


def registrarIngresosView(request, *args, **kwargs):
    
    if request.method == 'POST':
        if 'crear' in request.POST:
            form = RegistrarIngresosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/ingresos/')  # Pendiente a revisar
            else:
                messages.error(request, form.errors)
    else:
        form = RegistrarIngresosForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None), 'nombre_modelo': 'Ingreso'}

    return render(request, 'form.html', context)

def actualizarIngresosView(request, pk):
    instance = get_object_or_404(Ingresos, id=pk)
    if request.method == 'POST':
        form = RegistrarIngresosForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            return redirect('/ingresos/')  # Pendiente a revisar
        else:
            messages.error(request, form.errors)
    else:
        form = RegistrarIngresosForm(instance=instance)

    context = {'form': form, 'disabled': True, 'nombre_modelo': 'Ingreso'}

    return render(request, 'form.html', context)

def actualizarGastosView(request, pk):
    instance = get_object_or_404(Gastos, id=pk)
    if request.method == 'POST':
            form = RegistrarGastosForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/gastos/')  # Pendiente a revisar
            else:
                messages.error(request, form.errors)
    else:
        form = RegistrarGastosForm(instance=instance)

    context = {'form': form, 'disabled' : True, 'nombre_modelo': 'Gasto'}

    return render(request, 'form.html', context)

def registrarUsuarioView(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'websitepruebas2@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(
                request, f'Your account has been created ! You are now able to log in')
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'registroUsuario.html', {'form': form, 'title': 'reqister here'})


def login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        # if user is not NULL:
        #     form = login(request, user)
        #     messages.success(request, f' wecome {username} !!')
        #     return redirect('home')
        # else:
        #     messages.info(request, f'account done not exit pls sign in')
    form = AuthenticationForm()
    return render(request, 'inicio.html', {'form':form, 'title':'log in'})


def eliminarIngresosView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        Ingresos.objects.get(pk=pk).delete()
    return redirect('/ingresos/')

def eliminarGastosView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        Gastos.objects.get(pk=pk).delete()
    return redirect('/gastos/')