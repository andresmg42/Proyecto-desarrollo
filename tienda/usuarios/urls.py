from django.urls import path,include,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()

router.register(r'usuarios',views.UsuarioView, 'usuarios')


urlpatterns = [

    path("api/",include(router.urls)),
    
   # path("usuarios/docs/",include_docs_urls(title="API Usuarios")),
    re_path('login',views.login),
    re_path('register',views.register),
    re_path('profile',views.profile),

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)