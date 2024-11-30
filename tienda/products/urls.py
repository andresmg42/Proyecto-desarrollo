from django.urls import path
from . import views

urlpatterns = [
    path('administrador/categorias/', views.adminCategorias, name='Categorias'),
    path('administrador/ventas/', views.adminVentas, name='Ventas'),
    path('administrador/productos/', views.adminProductos, name='Productos'),
]