from django.shortcuts import render,redirect
from servicios.forms import InsumoForm, MarcaForm, ServicioForm
from servicios.models import Insumo, Marca, Servicio

# Create your views here.
def servicio (request):
    servicio_db = Servicio.objects.all()
    servicio = ServicioForm(request.POST or None, request.FILES or None)
    if servicio.is_valid():
       servicio.save()
       return redirect('servicio')
    context = {
        'servicio_db': servicio_db,
        'servicio': servicio,
    }
    return render (request, 'servicios/servicio.html', context)
# lOGICA DE insumo (EDITAR ELIMINAR Y OTRAS FUNCIONES)
def insumo(request):
    insumo_db = Insumo.objects.all()
    insumo = InsumoForm(request.POST or None, request.FILES or None)
    if insumo.is_valid():
        insumo.save()
        return redirect('insumo')
    context = {
        'insumo_db': insumo_db,	
        'insumo': insumo,
    }
    return render (request, 'servicios/insumo.html', context)

#def editarinsumo(request,id):
    edit_user = Insumo.objects.get(id=id)
    formulario = InsumoForm(request.POST or None, request.FILES or None, instance=edit_user)
    context = {
        'formulario': formulario,
    }
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('insumo')
    return render (request, 'servicios/insumo.html', context) 
     
#def eliminarinsumo(request,id):
    delete_user = Insumo.objects.get(id=id)
    url_back = 'insumo'
    txt_action = 'insumo'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST':
        delete_user.delete()
        return redirect ('insumo')  
    return render (request, 'servicios/insumo.html',context)

# LOGICA DE marca (EDITAR, ELIMINAR  Y OTRAS FUNCIONES)
def marca(request):
    marca_db = Marca.objects.all()
    marca = MarcaForm(request.POST or None)
    if marca.is_valid():
        marca.save()
        return redirect('marca')
    context = {
        'marca_dbs': marca_db,
        'marca': marca,
    }
    return render (request,'servicios/marca.html', context)


def editarMarca(request,id):
    edit_marca = Marca.objects.get(id=id)
    marca = MarcaForm(request.POST or None, instance=edit_marca)
    context={
        'marca': marca,
    }
    if marca.is_valid() and request.method == 'POST':
        marca.save()
        return redirect('marca')
    return render (request, 'servicios/marca.html', context)   

def eliminarMarca(request,id):
    delete_user = Marca.objects.get(id=id)
    url_back = 'marca'
    txt_action = 'marca'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST':
        delete_user.delete()
        return redirect ('insumo')  
    return render (request, 'servicios/deletemarca.html',context)