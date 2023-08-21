from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cliente
from .forms import clienteFormulario

# Create your views here.


def inicio(request):
    return render (request,"paginas/inicio.html")
def nosotros(request):
    return render (request,'paginas/nosotros.html')
def servicios(request):
    return render (request,'paginas/servicios.html')
def contactenos(request):
    return render (request,'paginas/contactenos.html')
def clientes(request):
    usuario= cliente.objects.all()
    print(usuario)
    return render (request,'basedatos/index.html',{'Usuarios':usuario})
def crearUsuario(request):
    formulario = clienteFormulario(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cliente')

    return render (request,'basedatos/crear.html',{'formulario': formulario})
def editarUsuario(request,id):
    usuario = cliente.objects.get(id=id)
    formulario = clienteFormulario(request.POST or None,request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cliente')
    return render (request,'basedatos/editar.html',{'formulario': formulario})

def eliminarUsuario(request,id):
    usuario=cliente.objects.get(id=id)
    usuario.delete()
    return redirect('cliente')
