from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductoSerializer
from .models import  Producto
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
        
class IsStaffOrSuperuserWriteOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permitir métodos de lectura (GET, HEAD, OPTIONS) para cualquiera
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Métodos de escritura solo para usuarios autenticados como staff o superusuarios
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    
    # Aplicar el permiso personalizado
    def get_authenticators(self):
        return super().get_authenticators()
    authentication_classes = [TokenAuthentication]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsStaffOrSuperuserWriteOnly]
            
        return [permission() for permission in permission_classes]
    


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
    