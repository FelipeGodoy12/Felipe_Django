from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index, name='index'),
    path('contacto',views.contacto, name='Contacto'),
    path('estadisticas',views.estadisticas, name='estadisticas'),
    path('formulario',views.formulario, name='formulario'),
    path('registrarse',views.registrar, name='registrase'),
    path('ingresado',views.ingresado, name='ingresado'),
    path('formulariomusico',views.formulariomusico, name='formulariomusico'),
]
