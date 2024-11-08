from django.db import models

class Usuario(models.Model):
    #id=models.CharField(max_length=10, unique=True,primary_key=True)
    nombre=models.CharField(max_length = 30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=10, verbose_name="Teléfono")
    contrasena=models.CharField(max_length = 10, verbose_name="Contraseña")
    foto= models.ImageField(upload_to='usuarios/', null=True, verbose_name="Foto de perfil")
    
    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
        
    def __str__(self):
        return self.nombre

# Create your models here.
