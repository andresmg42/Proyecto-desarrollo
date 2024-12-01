from rest_framework import viewsets
from .serializer import  CarritoSerializer
from .models import Carrito_compra



class CarritoView(viewsets.ModelViewSet):
    serializer_class=CarritoSerializer
    queryset=Carrito_compra.objects.all()