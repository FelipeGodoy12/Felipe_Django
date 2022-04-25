from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .forms import proveedorform, UserRegistrerForm, musicoform
from .models import Provedore, Musico

# Create your views here.
def index(request):
    return render(request, 'Miaplicacion/index.html')

def contacto(request):
    return render(request, 'Miaplicacion/Contacto.html')

def estadisticas(request):
    return render(request, 'Miaplicacion/estadisticas.html')

def formulario(request):

    form = proveedorform()
    if request.method == 'POST':
        form = proveedorform(request.POST)
        if form.is_valid():
            proveedor = Provedore()
            proveedor.nombre_proveedor = form.data['nombre_proveedor']
            proveedor.categoria = form.data['categoria']
            proveedor.direccion = form.data['direccion']
            proveedor.telefono_proveedor = form.data['telefono_proveedor']
            proveedor.email_proveedor = form.data['email_proveedor']
            proveedor.save()
            messages.success(request, f'El proveedor {proveedor.nombre_proveedor} a sido Registrado Correctamente')
        else:
            print('invalido')

    return render(request, 'Miaplicacion/formulario.html',{'form': form})

def formulariomusico(request):

    form = musicoform()
    if request.method == 'POST':
        form = musicoform(request.POST)
        if form.is_valid():
            proveedor = Musico()
            proveedor.nombre_musico = form.data['nombre_musico']
            proveedor.categoria = form.data['categoria']
            proveedor.direccion = form.data['direccion']
            proveedor.telefono_musico = form.data['telefono_musico']
            proveedor.email_musico = form.data['email_musico']
            proveedor.save()
            messages.success(request, f'El Músico {proveedor.nombre_musico} a sido Registrado Correctamente')
        else:
            print('invalido')

    return render(request, 'Miaplicacion/formulariomusico.html',{'form': form})


def registrar(request):
    if request.method == 'POST':
        form = UserRegistrerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El Usuario {username} a sido Registrado Correctamente')
            return redirect('login')
    else:
        form = UserRegistrerForm()

    context = {'form':form}

    return render(request, 'Miaplicacion/registrarse.html', context)


@login_required
def ingresado(request):
    messages.success(request, f'El Usuario {username} a sido Registrado Correctamente')
    return render(request, 'Miaplicacion/ingresado.html')