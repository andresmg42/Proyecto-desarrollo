from django.urls import path,include,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers

router=routers.DefaultRouter()

router.register(r'usuarios',views.UsuarioView, 'usuarios')


urlpatterns = [

    path("api/",include(router.urls)),
    
  
    path('login/',views.login, name='login'),
   
    # re_path('update/',views.updateUser),
    # re_path('profile/',views.profile),
    # path("api/filter_users/", views.search_users),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)