from rest_framework import viewsets
from .serializer import  PedidoSerializer
from .models import  Pedido


class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializer
    queryset=Pedido.objects.all()
