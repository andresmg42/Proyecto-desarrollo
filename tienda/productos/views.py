from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductoSerializer
from .models import  Producto
from rest_framework import status



    
class ProductoView(viewsets.ModelViewSet):
    serializer_class=ProductoSerializer
    queryset=Producto.objects.all()
    


@api_view(['GET'])
def get_products_by_category(request, category_id):
    products = Producto.objects.filter(categoria_id=category_id)  
    serializer = ProductoSerializer(instance=products, many=True)  
    for product in serializer.data:
        product['foto_producto'] = request.build_absolute_uri(product['foto_producto'])
    return Response({"products": serializer.data}, status=status.HTTP_200_OK)