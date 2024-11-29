from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categoria(models.Model):
    
    nombre_categoria=models.CharField(max_length=30, verbose_name="Nombre de la categoría")
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    

    def __str__(self):
        return self.nombre_categoria
    
class Producto(models.Model):
    
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_cid', verbose_name="Categoría")
    estado_producto=models.BooleanField(verbose_name="Disponible")
    nombre=models.CharField(max_length=30)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=50, verbose_name="Descripción")
    foto_producto=models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name="Foto del producto")
    cantidad_producto=models.IntegerField(verbose_name="Cantidad")
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    
    usuarios = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente_pid', verbose_name="Id del usuario")
    metodo_pago=models.CharField(max_length=30, verbose_name="Método de pago")
    productos=models.ManyToManyField(Producto,through='PedidoProducto')
    hora=models.TimeField(auto_now_add=True)
    estado_pedido=models.BooleanField(verbose_name="Envíado")
    fecha =models.DateField()
    
    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
    
    def __str__(self):
        return self.fecha.strftime("%Y-%m-%d %H:%M:%S")
    
class Carrito_compra(models.Model):
    productos=models.ManyToManyField(Producto,through='CarritoProducto')
    id_carrito=models.CharField(max_length=10, unique=True,primary_key=True)
    cantidad_total_productos=models.IntegerField()
    monto_carrito=models.DecimalField(max_digits=10, decimal_places=2)
    
 
    
class PedidoProducto(models.Model):
    pedido_ppid = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_ppid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito_compra, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField() 

