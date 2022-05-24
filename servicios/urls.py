from django.urls import path
from servicios.views import editarMarca, eliminarMarca, insumo, marca, servicio
urlpatterns = [
    path('servicio/',servicio, name='servicio'),
    path ('insumo/', insumo, name='insumo'),
    path ('marca/', marca, name='marca'),
    
    #EDITAR Y ELIMINAR MARCA
    path ('marca/editarMarca/<int:id>', editarMarca, name='editarMarca'),
    path ('marca/eliminarMarca/<int:id>', eliminarMarca, name='eliminarMarca'),
]