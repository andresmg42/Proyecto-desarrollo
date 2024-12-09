from rest_framework import viewsets
from .serializer import  PedidoSerializer, PedidoProductoSerializer
from .models import  Pedido, PedidoProducto


class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializer
    queryset=Pedido.objects.all()

class PedidoProductoView(viewsets.ModelViewSet):
    serializer_class=PedidoProductoSerializer
    queryset=PedidoProducto.objects.all()
