from django.db import models
from django.utils.translation import gettext_lazy as _
from servicios.models import Servicio

# Create your models here.
class DetalleFactura(models.Model):
    servicio=models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, verbose_name=u"Servicio")
    class Pago(models.TextChoices):
        VALOR1='', _('')
    pago=models.CharField(max_length=6, choices=Pago.choices,default=Pago.VALOR1, verbose_name="Pago")

#class Factura(models.Model):
    #numeroFactura =
    #fecha= models.DateField(auto_now=True, verbose_name="Fecha de Factura", help_text=u"MM/DD/AAAA")
    #nombre=models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,related_name='Nombre')
    #telefono=models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,related_name='Telefono')
    #placa=models.ForeignKey(Vehículo,on_delete=models.SET_NULL,null=True,related_name='Placa')
    #modelo=models.ForeignKey(Vehículo,on_delete=models.SET_NULL,null=True,related_name='Modelo')
    #servicio=models.ForeignKey(Servicio,on_delete=models.SET_NULL,null=True,related_name='Servicio')
    #pago=models.ForeignKey(DetalleFactura,on_delete=models.SET_NULL,null=True,vrelated_name='Pago')            