
from multiprocessing import context
from django.shortcuts import render, redirect
from registro.forms import usuarioForm, vehiculoForm
from registro.models import Usuario, Vehículo

# Create your views here.


# lOGICA DE USUARIO (EDITAR ELIMINAR Y OTRAS FUNCIONES)
def usuario(request):
    usuario_db = Usuario.objects.all()
    formulario = usuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuario')
    context = {
        'usuario_db': usuario_db,	
        'formulario': formulario,
    }
    return render (request, 'register/user.html', context)

def editarUsuario(request,id):
    edit_user = Usuario.objects.get(id=id)
    formulario = usuarioForm(request.POST or None, request.FILES or None, instance=edit_user)
    context = {
        'formulario': formulario,
    }
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('usuario')
    return render (request, 'register/user.html', context) 
     
def eliminarUsuario(request,id):
    delete_user = Usuario.objects.get(id=id)
    url_back = 'usuario'
    txt_action = 'Usuario'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST':
        delete_user.delete()
        return redirect ('usuario')  
    return render (request, 'register/deleteUser.html',context)

# LOGICA DE VEHICULO (EDITAR, ELIMINAR  Y OTRAS FUNCIONES)
def vehiculo(request):
    vehiculo_db = Vehículo.objects.all()
    vehiculo = vehiculoForm(request.POST or None)
    context = {
        'vehiculo_db': vehiculo_db,
        'vehiculo': vehiculo,
    }
    return render (request, 'register/vehiculo.html', context)


def editarVehiculo(request,id):
    edit_vehiculo = Vehículo.objects.get(id=id)
    formulario_vehiculo = vehiculoForm(request.POST or None, instance=edit_vehiculo)
    context={
        'formulario_vh': formulario_vehiculo,
    }
    if formulario_vehiculo.is_valid() and request.method == 'POST':
        formulario_vehiculo.save()
        return redirect('vehiculo')
    return render (request, 'register/vehiculo.html', context)  
#  edit_user = Usuario.objects.get(id=id)
#     formulario = usuarioForm(request.POST or None, request.FILES or None, instance=edit_user)
#     context = {
#         'formulario': formulario,
#     }
#     if formulario.is_valid() and request.method == 'POST':
#         formulario.save()
#         return redirect('usuario')
#     return render (request, 'register/user.html', context) 
     

def eliminarVehiculo(request,id):
    delete_vehiculo = Vehículo.objects.get(id=id)
    url_back = 'vehiculo'
    txt_action = 'vehiculo'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST':
        delete_vehiculo.delete()
        return redirect ('vehiculo')  
    return render (request, 'register/deletevehicle.html',context)



