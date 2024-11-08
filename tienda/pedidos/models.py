from django.db import models
from products.models import Producto 
from autenticacion.models import Usuario

class Pedido(models.Model):
    #id_compra=models.CharField(max_length=10, unique=True, primary_key=True, verbose_name="Id de la compra")
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cliente_pid', verbose_name="Id del usuario")
    metodo_pago=models.CharField(max_length=30, verbose_name="Método de pago")
    #monto_pedido= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad pedida")
    productos=models.ManyToManyField(Producto,through='PedidoProducto')
    hora=models.TimeField(auto_now_add=True)
    estado_pedido=models.BooleanField(verbose_name="Envíado")
    fecha =models.DateField()
    
    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
    
    def __str__(self):
        return self.fecha.strftime("%Y-%m-%d %H:%M:%S")
    
class PedidoProducto(models.Model):
    pedido_ppid = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_ppid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()

# Create your models here.
