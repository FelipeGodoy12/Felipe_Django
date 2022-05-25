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

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)    
    def __str__(self):
        return self.nombre_categoria

class Direccion(models.Model):
    numero_direccion = models.CharField(max_length=50)
    calle_direccion = models.CharField(max_length=50)
    ciudad_direccion = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.numero_direccion} {self.calle_direccion} {self.ciudad_direccion}'

class Provedore(models.Model):
    nombre_proveedor = models.CharField(max_length=60,verbose_name='Ingrese nombre del proveedor')
    categoria_proveedor = models.CharField(max_length=60,verbose_name='Ingrese categoria del proveedor')
    direccion_proveedor = models.OneToOneField(Direccion, null=True, on_delete=models.SET_NULL)
    telefono_proveedor = models.IntegerField(verbose_name='Ingrese Telefono del proveedor')
    email_proveedor = models.EmailField(verbose_name="Ingrese Correo del Proveedor")
    categoria_proveedor = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.nombre_proveedor

class Musico(models.Model):
    nombre_musico = models.CharField(max_length=60,verbose_name='Ingrese nombre del musico')
    categoria_musico = models.CharField(max_length=60,verbose_name='Ingrese categoria del musico')
    direccion_musico = models.CharField(max_length=60,verbose_name='Ingrese la direccion del musico')
    telefono_musico = models.IntegerField(verbose_name='Ingrese Telefono del musico')
    email_musico = models.EmailField(verbose_name="Ingrese Correo del musico")

    def __str__(self):
        return self.nombre_musico

class Audioyvideo(models.Model):
    nombre_audioyvideo = models.CharField(max_length=60, verbose_name='Ingrese nombre del Audio y video')
    categoria_audioyvideo = models.CharField(max_length=60,verbose_name='Ingrese categoria del Audio y video')
    direccion_audioyvideo = models.CharField(max_length=60,verbose_name='Ingrese la direccion del Audio y video')
    telefono_audioyvideo = models.IntegerField(verbose_name='Ingrese Telefono del Audio y video')
    email_audioyvideo = models.EmailField(verbose_name="Ingrese Correo del Audio y video")
    def __str__(self):
        return self.nombre_audioyvideo

class Comentarios(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.nombre