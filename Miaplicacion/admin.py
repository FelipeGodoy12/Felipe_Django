from django.contrib import admin
from . import models

# Register your models here.

class ProvedoreAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedor','categoria','direccion',)
    list_filter = ('categoria',)


admin.site.register(models.Provedore, ProvedoreAdmin)


admin.site.register(models.Cliente)
admin.site.register(models.Musico)
admin.site.register(models.Comentarios)