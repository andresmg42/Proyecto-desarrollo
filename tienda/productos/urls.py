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
    path("api/productos/get_by_name/<str:name>/",views.get_products_by_name),
    path("api/productos/get_by_precio/<str:precio>/",views.get_products_by_precio),
    path("api/productos/get_by_estado/<str:estado>/",views.get_products_by_estado),
    path("api/productos/get_by_cantidad/<int:cantidad>/",views.get_products_by_cantidad),
    #path("productos/docs/",include_docs_urls(title="API productos")),
    

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

