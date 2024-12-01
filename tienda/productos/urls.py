from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()

router.register(r'productos',views.ProductoView,'prodctos')


urlpatterns = [

    path("api/",include(router.urls)),
    path("api/productos/get_by_category/<int:category_id>/",views.get_products_by_category),
    #path("productos/docs/",include_docs_urls(title="API productos")),
    

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)