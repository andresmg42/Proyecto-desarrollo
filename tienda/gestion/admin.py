from django.contrib import admin
from gestion.models import Producto, Categoria, Usuario, PedidoProducto,Pedido

class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "precio")

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("nombre_categoria",)
    search_fields = ("nombre_categoria",)

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email",)
    search_fields = ("nombre", "email",)

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1

class PedidosAdmin(admin.ModelAdmin):
    list_display = (  "fecha", "mostrar_productos", "estado_pedido",)
    search_fields = ("usuarios_nombre", "mostrar_productos",)
    list_filter = ("fecha",)
    date_hierarchy = "fecha"
    inlines = [PedidoProductoInline]

    def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])

    mostrar_productos.short_description = "Productos"


    
    
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Categoria, CategoriasAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(Pedido, PedidosAdmin)



