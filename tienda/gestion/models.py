from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    id=models.CharField(max_length=10, unique=True,primary_key=True)
    nombre=models.CharField(max_length = 30)
    direccion=models.CharField
    email=models.EmailField()
    tfno=models.CharField(max_length=10)
    contrasena=models.CharField(max_length = 10)
    foto= models.ImageField(upload_to='usuarios/', null=True)

class Categoria(models.Model):
    id_categoria=models.CharField(max_length=10, unique=True,primary_key=True)
    nombre_categoria=models.CharField(max_length=10)
    
class Producto(models.Model):
    
    id_producto=models.CharField(max_length=10, unique=True, primary_key=True)
    categoria_cid = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_cid')
    estado_producto=models.BooleanField()
    nombre=models.CharField(max_length=30)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=50)
    foto_producto=models.ImageField(upload_to='productos/', null=True, blank=True)
    cantidad_producto=models.IntegerField()
    



class Pedido(models.Model):
    id_compra=models.CharField(max_length=10, unique=True, primary_key=True)
    usuario_pid = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cliente_pid')
    metodo_pago=models.CharField(max_length=30)
    monto_pedido= models.DecimalField(max_digits=10, decimal_places=2)
    productos=models.ManyToManyField(Producto,through='PedidoProducto')
    hora=models.TimeField(auto_now_add=True)
    estado_pedido=models.BooleanField()
    fecha =models.DateField()
    
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
    carrito_cppid = models.ForeignKey(Carrito_compra, on_delete=models.CASCADE)
    producto_cppid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField() 

   

# Create your models here.
