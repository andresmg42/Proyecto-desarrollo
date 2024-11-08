from django.contrib import admin
from autenticacion.models import Usuario

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email",)
    search_fields = ("nombre", "email",)

admin.site.register(Usuario, UsuariosAdmin)

# Register your models here.
