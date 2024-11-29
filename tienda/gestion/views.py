from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UsuarioSerializer, CategoriaSerializer, ProductoSerializer, PedidoSerializer, CarritoSerializer
from .models import Categoria, Producto, Pedido, Carrito_compra
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UsuarioView(viewsets.ModelViewSet):
    serializer_class=UsuarioSerializer
    queryset=User.objects.all()

class CategoriaView(viewsets.ModelViewSet):
    serializer_class=CategoriaSerializer
    queryset=Categoria.objects.all()
    
class ProductoView(viewsets.ModelViewSet):
    serializer_class=ProductoSerializer
    queryset=Producto.objects.all()
    
class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializer
    queryset=Pedido.objects.all()

class CarritoView(viewsets.ModelViewSet):
    serializer_class=CarritoSerializer
    queryset=Carrito_compra.objects.all()

#login

@api_view(['POST'])
def login(request):
    
    user=get_object_or_404(User,username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({"error":"invalid password"},status=status.HTTP_400_BAD_REQUEST)
    
    token,created= Token.objects.get_or_create(user=user)
    serializer=UsuarioSerializer(instance=user)
    
    return Response({"token":token.key, "user":serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer=UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        user=User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        
        token=Token.objects.create(user=user)
        
        return Response({'token':token.key,'user':serializer.data},status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.user.id)
    return Response("you are login with {}".format(request.user.username),status=status.HTTP_200_OK)