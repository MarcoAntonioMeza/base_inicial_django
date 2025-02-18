
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path("direccion/", include("apps.direccion.urls")),
    path("usuario/", include("apps.usuario.urls")),
    
]
