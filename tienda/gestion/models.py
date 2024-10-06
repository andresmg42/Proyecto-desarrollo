from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    id=models.CharField(max_length=10, unique=True)
    nombre=models.CharField(max_length = 30)
    direccion=models.CharField
    email=models.EmailField()
    tfno=models.CharField(max_length=10)
    contrasena=models.CharField(max_length = 10)
    foto= models.ImageField(upload_to='usuarios/', null=True, blank=True)
    
class Cliente(models.Model):
    pass
    
class Administrador(models.Model):
    reporte = models.CharField(max_length = 100)

class Pedido(models.Model):
    id_compra=models.CharField(max_length=10, unique=True)
    cliente_pid = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_pid')
    metodo_pago=models.CharField(max_length=30)
    monto_pedido= models.DecimalField(max_digits=10, decimal_places=2)
    hora=models.TimeField(auto_now_add=True)
    estado_pedido=models.BooleanField()
    fecha =models.DateField()
    
class Carrito_compra(models.Model):
    id_carrito=models.CharField(max_length=10, unique=True)
    cantidad_total_productos=models.IntegerField()
    monto_carrito=models.DecimalField(max_digits=10, decimal_places=2)
    
class Categoria(models.Model):
    id_categoria=models.CharField(max_length=10, unique=True)
    nombre_categoria=models.CharField(max_length=10)

class Producto(models.Model):
    
    id_producto=models.CharField(max_length=10, unique=True)
    carrito_ccid = models.ForeignKey(Carrito_compra, on_delete=models.CASCADE, related_name='carrito_ccid')
    admin_aid = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='admin_aid')
    pedido_pid = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedido_pid')
    categoria_cid = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_cid')
    estado_producto=models.BooleanField()
    nombre=models.CharField(max_length=30)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=50)
    foto_producto=models.ImageField(upload_to='productos/', null=True, blank=True)
    cantidad_producto=models.IntegerField()
    
class UsuarioProducto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_usuario=models.IntegerField()

class CarritoProducto(models.Model):
    Carrito = models.ForeignKey(Carrito_compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()
class PedidoProducto(models.Model):
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()
    

   

# Create your models here.
