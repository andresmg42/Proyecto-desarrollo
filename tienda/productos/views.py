from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductoSerializer
from .models import  Producto
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes,action
from rest_framework.permissions import IsAuthenticated,BasePermission,IsAdminUser
from rest_framework.authentication import TokenAuthentication




class IsClient(BasePermission):
    """
    Permite que usuarios con is_staff=True solo puedan leer o crear.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user.is_staff:
            return view.action in ['list','retrieve']
        
        return True
        
class ProductoView(viewsets.ModelViewSet):
    serializer_class=ProductoSerializer
    queryset=Producto.objects.all()
    # authentication_classes=[TokenAuthentication]
    permission_classes=[IsClient]
    


@api_view(['GET'])
def search_products(request):
    
    criteria = request.GET.get('criteria')
    value = request.GET.get('value')
    
    print("criteria= ",criteria)
    print("value= ",value)
    
    if not criteria or not value:
        return Response({"error": "Missing criteria or value"}, status=400)

    # Mapea los criterios a los campos del modelo
  
    
    match criteria:
        case 'categoria_id':
            value=int(value)
        case 'cantidad_producto':
            value=int(value)
            
        case 'estado_producto':
            
            value = value.lower()=='activo'
            
            
        case 'precio':
            value=float(value)
        
        case 'nombre':
            criteria='nombre__icontains'
            
        
        case _:
            value=value
    


    filter_args = {criteria: value}
    products = Producto.objects.filter(**filter_args)
    serializer = ProductoSerializer(instance=products, many=True)  
    for product in serializer.data:
        product['foto_producto'] = request.build_absolute_uri(product['foto_producto'])
    return Response({"products": serializer.data}, status=status.HTTP_200_OK)
    