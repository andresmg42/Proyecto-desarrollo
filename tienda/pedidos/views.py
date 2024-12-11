from rest_framework import viewsets
from .serializer import  PedidoSerializer, PedidoProductoSerializer
from .models import  Pedido, PedidoProducto
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response




class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializer
    queryset=Pedido.objects.all()

class PedidoProductoView(viewsets.ModelViewSet):
    serializer_class=PedidoProductoSerializer
    queryset=PedidoProducto.objects.all()

@api_view(['GET'])
def send_email_cancel(request):
    dest = request.GET.get('dest')
    mensaje = request.GET.get('mensaje')
    
    if not dest or not mensaje:
        return Response({'error': 'Missing dest or mensaje parameter'}, status=400)
    
    try:
        send_mail(
            'Pedido cancelado',
            mensaje, 
            'andresdavid.ortega@gmail.com',
            [dest],
            fail_silently=False,
        )
        return Response({'success': 'Email sent successfully'})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
