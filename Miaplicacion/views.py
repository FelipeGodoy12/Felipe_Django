from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .forms import proveedorform, UserRegistrerForm
from .models import Provedore

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
    return render(request, 'Miaplicacion/ingresado.html')