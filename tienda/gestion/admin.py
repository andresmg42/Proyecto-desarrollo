from django.contrib import admin
from gestion.models import Producto, Categoria, Usuario, Pedido

class ProductosAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "nombre", "categoria_cid", "precio")
    list_filter = ("categoria_cid",)
    search_fields = ("id_producto","nombre", "categoria_cid", "precio")

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre_categoria")
    search_fields = ("id_categoria", "nombre_categoria")

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion", "email")
    search_fields = ("id","nombre", "email")

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id_compra", "usuario_pid", "fecha", "mostrar_productos", "estado_pedido")
    search_fields = ("id_compra", "usuario_pid", "productos")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

    def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])

    mostrar_productos.short_description = "Productos"


admin.site.register(Producto, ProductosAdmin)
admin.site.register(Categoria, CategoriasAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(Pedido, PedidosAdmin)

