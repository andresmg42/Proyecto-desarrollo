from rest_framework import serializers
from .models import Carrito_compra


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrito_compra
        fields= '__all__'