from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .forms import proveedorform, UserRegistrerForm, musicoform, audioyvideoform, ComentarioForm
from .models import Provedore, Musico, Comentarios, Audioyvideo

# Create your views here.
def index(request):
    return render(request, 'Miaplicacion/index.html')

def contacto(request):
    return render(request, 'Miaplicacion/Contacto.html')

def estadisticas(request):
    return render(request, 'Miaplicacion/estadisticas.html')

def formularioproveedor(request):

    form = proveedorform()
    if request.method == 'POST':
        form = proveedorform(request.POST)
        if form.is_valid():
            proveedor = Provedore()
            proveedor.nombre_proveedor = form.data['nombre_proveedor']
            proveedor.categoria_proveedor = form.data['categoria_proveedor']
            proveedor.direccion_proveedor = form.data['direccion_proveedor']
            proveedor.telefono_proveedor = form.data['telefono_proveedor']
            proveedor.email_proveedor = form.data['email_proveedor']
            proveedor.save()
            messages.success(request, f'El proveedor {proveedor.nombre_proveedor} a sido Registrado Correctamente')
        else:
            print('invalido')

    return render(request, 'Miaplicacion/formularioproveedor.html',{'form': form})

def formulariomusico(request):

    form = musicoform()
    if request.method == 'POST':
        form = musicoform(request.POST)
        if form.is_valid():
            proveedor = Musico()
            proveedor.nombre_musico = form.data['nombre_musico']
            proveedor.categoria_musico = form.data['categoria_musico']
            proveedor.direccion_musico = form.data['direccion_musico']
            proveedor.telefono_musico = form.data['telefono_musico']
            proveedor.email_musico = form.data['email_musico']
            proveedor.save()
            messages.success(request, f'El Músico {proveedor.nombre_musico} a sido Registrado Correctamente')
        else:
            print('invalido')

    return render(request, 'Miaplicacion/formulariomusico.html',{'form': form})

def formularioaudioyvideo(request):

    form = audioyvideoform()
    if request.method == 'POST':
        form = audioyvideoform(request.POST)
        if form.is_valid():
            proveedor = Audioyvideo()
            proveedor.nombre_audioyvideo = form.data['nombre_audioyvideo']
            proveedor.categoria_audioyvideo = form.data['categoria_audioyvideo']
            proveedor.direccion_audioyvideo = form.data['direccion_audioyvideo']
            proveedor.telefono_audioyvideo = form.data['telefono_audioyvideo']
            proveedor.email_audioyvideo = form.data['email_audioyvideo']
            proveedor.save()
            messages.success(request, f'El Audio y video {proveedor.nombre_audioyvideo} a sido Registrado Correctamente')
        else:
            print('invalido')

    return render(request, 'Miaplicacion/formularioaudioyvideo.html',{'form': form})

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

def proveedores(request):

    proveedores = Provedore.objects.all()
    
    return render(request, 'Miaplicacion/proveedores.html',{'proveedores':proveedores})

def musicos(request):

    musicos = Musico.objects.all()
    
    return render(request, 'Miaplicacion/musicos.html',{'musicos':musicos})

def audioyvideos(request):

    audioyvideos = Audioyvideo.objects.all()
    
    return render(request, 'Miaplicacion/audioyvideos.html',{'audioyvideos':audioyvideos})



@login_required
def ingresado(request):
    messages.success(request, f'El Usuario a sido Registrado Correctamente')
    return render(request, 'Miaplicacion/ingresado.html')

def crearcomentario(request):

    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(data=request.POST)
        comentario = form.save(commit=False)
        comentario.save()
        return redirect('listarcomentarios')

    else:
        return render(request, 'Miaplicacion/crearcomentario.html', {'form':form})

def listarcomentarios(request):
        
    comentario = Comentarios.objects.all()

    return render(request, 'Miaplicacion/listarcomentarios.html', {'comentario':comentario})

def editarcomentarios(request, id):
    comentario = Comentarios.objects.get(pk=id)

    form = ComentarioForm(instance=comentario)
    if request.method == 'POST':
        form = ComentarioForm(data=request.POST, instance=comentario)
        form.save()
        return redirect('listarcomentarios')

    else:
        return render(request, 'Miaplicacion/editarcomentarios.html', {'form':form})

def eliminarcomentario(request, id):
    comentario = Comentarios.objects.get(pk=id)
    comentario.delete()
    return redirect('listarcomentarios')