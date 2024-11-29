from rest_framework import serializers
from .models import Categoria, Producto, Pedido, Carrito_compra
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id','username','email','password']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields= '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields= '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields= '__all__'
        
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedido
        fields= '__all__'
        
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrito_compra
        fields= '__all__'