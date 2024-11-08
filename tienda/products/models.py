from django.db import models

class Categoria(models.Model):
    #id_categoria=models.CharField(max_length=10, unique=True,primary_key=True, verbose_name="Id de la categoría")
    nombre_categoria=models.CharField(max_length=10, verbose_name="Nombre de la categoría")
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    #id_producto=models.CharField(max_length=10, unique=True, primary_key=True, verbose_name="Id del producto")
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

# Create your models here.
