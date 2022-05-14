from django.shortcuts import redirect, render
from facturacion.forms import DetalleFacturaForm

from facturacion.models import DetalleFactura

def detalleFactura(request):
    detalle_db = DetalleFactura.objects.all()
    detalle = DetalleFacturaForm(request.POST or None)
    context = {
        'detalle_db': detalle_db,	
        'detalle': detalle,
    }
    return render (request, 'facturacion/detalleFactura.html', context)

#def factura(request):
    factura_db = Factura.objects.all()
    formulario = FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('factura')
    context = {
        'factura_db': factura_db,	
        'formulario': formulario,
    }
    return render (request, 'facturacion/factura.html', context)

