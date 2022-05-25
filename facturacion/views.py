from django.shortcuts import redirect, render
from facturacion.forms import DetalleFacturaForm,FacturaForm

from facturacion.models import DetalleFactura,Factura

def detalleFactura(request):
    detalle_db = DetalleFactura.objects.all()
    detalle = DetalleFacturaForm(request.POST or None, request.FILES or None)
    if detalle.is_valid():
       detalle.save()
       return redirect('detalleFactura')
    context = {
        'detalle_db': detalle_db,	
        'detalle': detalle,
    }
    return render (request, 'facturacion/detalleFactura.html', context)
def editarDetalleFa(request,id):
    edit_DetalleFa = DetalleFactura.objects.get(id=id)
    detalle = DetalleFacturaForm(request.POST or None, request.FILES or None, instance=edit_DetalleFa)
    context = {
        'detalle': detalle,
    }
    if detalle.is_valid() and request.method == 'POST':
        detalle.save()
        return redirect('detalleFactura')
    return render (request, 'facturacion/detalleFactura.html', context) 
     
def eliminarDetalleFa(request,id):
    delete_detalle = DetalleFactura.objects.get(id=id)
    url_back = 'detalle'
    txt_action = 'detalleFactura'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST':
        delete_detalle.delete()
        return redirect ('detalleFactura') 
    return render (request, 'facturacion/deletedetalle.html',context)
def factura(request):
    factura_db = Factura.objects.all()
    facturas= FacturaForm(request.POST or None, request.FILES or None)
    if facturas.is_valid():
        facturas.save()
        return redirect('factura')
    context = {
        'factura_db': factura_db,	
        'facturas': facturas,
    }
    return render (request, 'facturacion/factura.html', context)

