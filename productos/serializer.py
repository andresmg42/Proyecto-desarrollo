from rest_framework import serializers
from .models import  Producto,ProductoUsuario,Favoritos
from django.contrib.auth.models import User

      
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields= '__all__'
        
        
class UserProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductoUsuario
        fields= '__all__'

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favoritos
        fields= '__all__'
        
