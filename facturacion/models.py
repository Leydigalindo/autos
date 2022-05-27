from django.db import models
from django.utils.translation import gettext_lazy as _
from servicios.models import Servicio
from registro.models import Usuario,Vehículo
# Create your models here.
class DetalleFactura(models.Model):
    servicio=models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, verbose_name=u"Servicio")
    pago=models.IntegerField(max_length=5,default='0', verbose_name="Pago")
    def __str__(self) -> str:
            return '%s' %(self.servicio)

class Factura(models.Model):
    fecha= models.DateField(auto_now=True, verbose_name="Fecha de Factura", help_text=u"MM/DD/AAAA")
    cliente=models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,related_name='Cliente')
    telefono=models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,related_name='Telefono')
    placa=models.ForeignKey(Vehículo,on_delete=models.SET_NULL,null=True,related_name='Placa')
    modelo=models.ForeignKey(Vehículo,on_delete=models.SET_NULL,null=True,related_name='Modelo')
    servicio=models.ForeignKey(Servicio,on_delete=models.SET_NULL,null=True,related_name='Servicio')
    pago=models.ForeignKey(DetalleFactura,on_delete=models.SET_NULL,null=True,related_name='Pago')            
   