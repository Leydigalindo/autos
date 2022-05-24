from django.contrib import admin
from .models import Servicio, Marca, Insumo 
# Register your models here.
admin.site.register(Servicio)
admin.site.register(Insumo)
admin.site.register(Marca)
