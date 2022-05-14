from django.urls import path
from servicios.views import insumo, marca, servicio
urlpatterns = [
    path('servicio/',servicio, name='servicio'),
    path ('insumo/', insumo, name='insumo'),
    path ('marca/', marca, name='marca'),
]