from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index, name='index'),
    path('contacto',views.contacto, name='Contacto'),
    path('estadisticas',views.estadisticas, name='estadisticas'),
    path('formularioproveedor',views.formularioproveedor, name='formularioproveedor'),
    path('registrarse',views.registrar, name='registrase'),
    path('ingresado',views.ingresado, name='ingresado'),
    path('proveedores',views.proveedores, name='proveedores'),
    path('musicos',views.musicos, name='musicos'),
    path('audioyvideos',views.audioyvideos, name='audioyvideos'),
    path('formulariomusico',views.formulariomusico, name='formulariomusico'),
    path('formularioaudioyvideo',views.formularioaudioyvideo, name='formularioaudioyvideo'),
    path('crearcomentario',views.crearcomentario, name='crearcomentario'),
    path('listarcomentarios',views.listarcomentarios, name='listarcomentarios'),
    path('editarcomentarios/<int:id>',views.editarcomentarios, name='editarcomentarios'),
    path('eliminarcomentarios/<int:id>',views.eliminarcomentario, name='eliminarcomentarios'),
]
