from rest_framework import viewsets
from .serializer import  PedidoSerializer, PedidoProductoSerializer, ProductosMasVendidosSerializer
from .models import  Pedido, PedidoProducto
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes,api_view
from rest_framework.response import Response
from django.db.models import Count,Sum
from productos.models import Producto
from productos.serializer import ProductoSerializer
from django.http import JsonResponse
from django.db.models import F,Sum

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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def productosMasVendidos(request):
   
    resultados = (
        Producto.objects
        .annotate(total_vendidos=Sum('pedidoproducto__cantidad_producto_carrito'))
        .values('id','nombre', 'precio', 'total_vendidos','estado_producto','descripcion','cantidad_producto')
        .order_by('-total_vendidos')
    )
      
    
    for resultado in resultados:
        resultado['ingresos']=resultado['precio']*resultado['total_vendidos']
    
    
        jsonData=resultados.values_list
    
    return Response(resultados,status=200)    
    
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def ventas_totales_metodo_pago(request):
    
    resultados= Pedido.objects.values('metodo_pago').annotate(
        total_pedidos=Count('id'),
        total_ventas=Sum('pedidoproducto__cantidad_producto_carrito' * F('pedido__producto__precio'))
        )
    
    return Response(resultados.values_list,status=200)
    
