from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    mail = models.EmailField(verbose_name="Ingrese Correo del Cliente")
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Provedore(models.Model):
    nombre_proveedor = models.CharField(max_length=60,verbose_name='Ingrese nombre del proveedor')
    categoria = models.CharField(max_length=60,verbose_name='Ingrese categoria del proveedor')
    direccion = models.CharField(max_length=60,verbose_name='Ingrese la direccion del proveedor')
    telefono_proveedor = models.IntegerField(verbose_name='Ingrese Telefono del proveedor')
    email_proveedor = models.EmailField(verbose_name="Ingrese Correo del Proveedor")

    def __str__(self):
        return self.nombre_proveedor

class Musico(models.Model):
    nombre_musico = models.CharField(max_length=60,verbose_name='Ingrese nombre del musico')
    categoria = models.CharField(max_length=60,verbose_name='Ingrese categoria del musico')
    direccion = models.CharField(max_length=60,verbose_name='Ingrese la direccion del musico')
    telefono_musico = models.IntegerField(verbose_name='Ingrese Telefono del musico')
    email_musico = models.EmailField(verbose_name="Ingrese Correo del musico")

    def __str__(self):
        return self.nombre_musico

class Comentarios(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.nombre