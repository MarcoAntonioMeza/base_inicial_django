
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404, handler500, handler403, handler400
from apps.adminv2.views import pag_404_not_found
from apps.usuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path("adminv2/", include("apps.adminv2.urls")),
    path("direccion/", include("apps.direccion.urls")),
    path("usuario/", include("apps.usuario.urls")),
    
]
