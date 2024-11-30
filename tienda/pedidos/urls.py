from django.urls import path
from . import views


urlpatterns = [
    path('administrador/pedidos/', views.adminPedidos, name='Pedidos'),
]