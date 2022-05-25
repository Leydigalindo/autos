from django import forms
from facturacion.models import DetalleFactura,Factura

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model=DetalleFactura
        fields ='__all__'

class FacturaForm(forms.ModelForm):
    class Meta:
       model=Factura
       fields='__all__'