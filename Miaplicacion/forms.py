from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Musico, Provedore, Comentarios
    
    
class proveedorform(forms.ModelForm):
    class Meta:
        model = Provedore
        fields = ("nombre_proveedor", "categoria", "direccion", "telefono_proveedor", "email_proveedor",)

class musicoform(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ("nombre_musico", "categoria", "direccion", "telefono_musico", "email_musico",)



class UserRegistrerForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =  ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'email', 'comentario']



