from django.urls import path

from facturacion.views import detalleFactura

urlpatterns = [
    path('detalleFactura/',detalleFactura, name='detalleFactura'),
    #path ('Factura/', factura, name='insumo'),
]