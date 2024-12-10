from rest_framework import viewsets
from .serializer import  PedidoSerializer, PedidoProductoSerializer
from .models import  Pedido, PedidoProducto
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes,api_view
from rest_framework.response import Response

class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializer
    queryset=Pedido.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    


class PedidoProductoView(viewsets.ModelViewSet):
    serializer_class=PedidoProductoSerializer
    queryset=PedidoProducto.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def llenarTablaProductosPedidos(request):
    
    data=request.data
    for element in data:
        serializer= PedidoProductoSerializer(data=element)
        if serializer.is_valid():
            serializer.save()
    return Response({'los datos fueron guardados con exito'},status=200)

        
        
    
    
