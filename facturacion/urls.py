from django.urls import path

from facturacion.views import detalleFactura,eliminarDetalleFa,editarDetalleFa,factura

urlpatterns = [
    path ('detalleFactura/',detalleFactura, name='detalleFactura'),
    path ('detalleFactura/eliminarDetalleFa/<int:id>', eliminarDetalleFa, name='eliminarDetalleFa'),
    path ('detalleFactura/editarDetalleFa/<int:id>', editarDetalleFa, name='editarDetalleFa'),
    path ('factura/',factura, name='factura'),
]