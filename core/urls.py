
from django.contrib import admin
from django.urls import include, path
from core import views
from core.views import home, manual

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('registro/', include('registro.urls')),
    path('servicio/',include('servicios.urls')),
    path('factura/',include("facturacion.urls")),
    path('manual', views.manual, name='manual'),
    # path('factura/', include('')) guia para incluir las urls de sus aplicaciones 
    
]


