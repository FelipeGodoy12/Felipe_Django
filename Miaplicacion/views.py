from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Miaplicacion/index.html')

def formulario(request):
    return render(request, 'Miaplicacion/formulario.html')