from django.contrib import admin
from products.models import Producto, Categoria

class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "precio")

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("nombre_categoria",)
    search_fields = ("nombre_categoria",)

admin.site.register(Producto, ProductosAdmin)
admin.site.register(Categoria, CategoriasAdmin)

# Register your models here.
