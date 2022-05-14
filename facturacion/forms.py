from django import forms
from facturacion.models import DetalleFactura

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model=DetalleFactura
        fields =['servicio','pago']

#class FacturaForm(forms.ModelForm):
    #class Meta:
       # model=Factura
        #fields=['nombre','telefono','placa','modelo','servicio','pago']