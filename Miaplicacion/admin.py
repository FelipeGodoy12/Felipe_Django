from django.contrib import admin
from . import models

# Register your models here.

class ProvedoreAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedor','categoria_proveedor','direccion_proveedor',)
    list_filter = ('categoria_proveedor',)


admin.site.register(models.Provedore, ProvedoreAdmin)

admin.site.register(models.Categoria)
admin.site.register(models.Direccion)

admin.site.register(models.Audioyvideo)
admin.site.register(models.Cliente)
admin.site.register(models.Musico)
admin.site.register(models.Comentarios)