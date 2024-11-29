from django.urls import path,include,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()

router.register(r'usuarios',views.UsuarioView, 'usuarios')
router.register(r'categorias', views.CategoriaView,'categorias')
router.register(r'productos',views.ProductoView,'prodctos')
router.register(r'pedidos',views.PedidoView,'pedidos')
router.register(r'carrito',views.CarritoView,'carrito')

urlpatterns = [

    path("api/",include(router.urls)),
    path("docs/",include_docs_urls(title="Gestion API")),
    re_path('login',views.login),
    re_path('register',views.register),
    re_path('profile',views.profile),

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)