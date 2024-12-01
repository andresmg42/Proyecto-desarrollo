from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()

router.register(r'carrito',views.CarritoView,'carrito')

urlpatterns = [

    path("api/",include(router.urls)),
    #path("carrito/docs/",include_docs_urls(title="API carrito")),
    

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)