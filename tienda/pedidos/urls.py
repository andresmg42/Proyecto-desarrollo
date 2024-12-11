from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()

router.register(r'pedidos',views.PedidoView,'pedidos')
router.register(r'pedidos_productos',views.PedidoProductoView,'pedidos_productos')


urlpatterns = [

    path("api/",include(router.urls)),
    path("api/send_email_cancel/", views.send_email_cancel,name='send_email_cancel'),
    #path("pedidos/docs/",include_docs_urls(title="API Pedidos")),
    

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)