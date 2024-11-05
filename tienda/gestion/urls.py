from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home,name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('administrador/', views.adminInicio, name='Admin'),
    path('administrador/categorias/', views.adminCategorias, name='Categorias'),
    path('administrador/ventas/', views.adminVentas, name='Ventas'),
    path('administrador/usuarios/', views.adminUsuarios, name='Usuarios'),
    path('administrador/productos/', views.adminProductos, name='Productos'),
    path('administrador/pedidos/', views.adminPedidos, name='Pedidos'),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)