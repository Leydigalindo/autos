from django.urls import path    
from . import views

urlpatterns = [
    path ('usuario/', views.usuario, name='usuario'),
    path ('vehiculo/', views.vehiculo, name='vehiculo'),
    path ('vehiculo/eliminarVehiculo/<int:id>', views.eliminarVehiculo, name='eliminarVehiculo'),
    path ('vehiculo/editarvehiculo/<int:id>', views.editarVehiculo, name='editarVehiculo'),
    path ('usuario/editarusuario/<int:id>', views.editarUsuario, name='editarUsuario'),
    path ('usuario/eliminarusuario/<int:id>', views.eliminarUsuario, name='eliminarUsuario'),
 ]