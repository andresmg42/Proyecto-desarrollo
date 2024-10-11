from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id=models.CharField(max_length=10, unique=True,primary_key=True)
    nombre=models.CharField(max_length = 30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=10, verbose_name="Teléfono")
    contrasena=models.CharField(max_length = 10, verbose_name="Contraseña")
    foto= models.ImageField(upload_to='usuarios/', null=True, verbose_name="Foto de perfil")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria=models.CharField(max_length=10, unique=True,primary_key=True, verbose_name="Id de la categoría")
    nombre_categoria=models.CharField(max_length=10, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombre_categoria
    
class Producto(models.Model):
    
    id_producto=models.CharField(max_length=10, unique=True, primary_key=True, verbose_name="Id del producto")
    categoria_cid = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_cid', verbose_name="Categoría")
    estado_producto=models.BooleanField(verbose_name="Disponible")
    nombre=models.CharField(max_length=30)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=50, verbose_name="Descripción")
    foto_producto=models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name="Foto del producto")
    cantidad_producto=models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    id_compra=models.CharField(max_length=10, unique=True, primary_key=True, verbose_name="Id de la compra")
    usuario_pid = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cliente_pid', verbose_name="Id del usuario")
    metodo_pago=models.CharField(max_length=30, verbose_name="Método de pago")
    monto_pedido= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad pedida")
    productos=models.ManyToManyField(Producto,through='PedidoProducto')
    hora=models.TimeField(auto_now_add=True)
    estado_pedido=models.BooleanField(verbose_name="Envíado")
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

