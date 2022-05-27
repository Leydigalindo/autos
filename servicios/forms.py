from django import forms

from servicios.models import Insumo, Marca, Servicio,DetalleInsumo

class ServicioForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields=['nombre','tipodeservicio']
        #fields= '__all__'
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields=['nombre','cantidad','marca']
    
        #fields = '__all__'
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields=['nombre','precio']
        #fields = '__all__'
class DetalleInsumoForm(forms.ModelForm):
    
    class Meta:
        model = Insumo
        fields = '__all__'   
    