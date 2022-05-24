from tkinter.ttk import Widget
from django import forms
from .models import Usuario, Vehículo

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class vehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehículo
        fields = '__all__'
        widgets = {
             'fecha':forms.DateInput(format=('%m/%d%y'),
                                     attrs ={'placeholder':'Seleccione una fecha','type':'date'}) 
        }

    