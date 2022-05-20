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

    