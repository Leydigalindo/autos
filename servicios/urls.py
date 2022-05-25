from django.urls import path
from servicios.views import editarMarca, eliminarMarca, insumo, marca, servicio,eliminarInsumo,editarInsumo,eliminarServicio,editarServicio
urlpatterns = [
    path('servicio/',servicio, name='servicio'),
    path ('insumo/', insumo, name='insumo'),
    path ('marca/', marca, name='marca'),
    
    #EDITAR Y ELIMINAR MARCA
    path ('marca/editarMarca/<int:id>', editarMarca, name='editarMarca'),
    path ('marca/eliminarMarca/<int:id>', eliminarMarca, name='eliminarMarca'),
    path ('insumo/eliminarInsumo/<int:id>', eliminarInsumo, name='eliminarInsumo'),
    path ('insumo/editarInsumo/<int:id>', editarInsumo, name='editarInsumo'),
    path ('servicio/eliminarServicio/<int:id>', eliminarServicio, name='eliminarServicio'),
    path ('servicio/editarServicio/<int:id>', editarServicio, name='editarServicio'),
]