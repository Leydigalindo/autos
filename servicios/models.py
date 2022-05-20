from logging import PercentStyle
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class Servicio(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= True, verbose_name=u"Nombre")
    class Tipodeservicio (models.TextChoices):
        EXCELENTE = 'Excelente', _('EXCELENTE')
        REGULAR= 'Regular', _('REGULAR')
        MALO = 'Malo', _('MALO')
    tipodeservicio = models.FieldChoice(seq)(max_length=10, choices=Tipodeservicio.choices, verbose_name=u"Seleccione el tipo de servicio")

    def __self__(self) -> str:
        return '%s'%(self.nombre)

class Marca(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Nombre")
    precio=models.IntegerField(default='0', verbose_name="Precio")
    
    def __str__(self) -> str:
            return '%s'%(self.nombre)
class Insumo(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Nombre")
    cantidad= models.PositiveIntegerField(validators=[MinValueValidator(1)])
    marca=models.ForeignKey(Marca,on_delete=models.SET_NULL, null=True,verbose_name=u"Marca")

    def __str__(self) -> str:
            return '%s'%(self.nombre)

