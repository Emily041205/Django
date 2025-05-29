
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Vista para listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar.html', {'productos': productos})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')

        producto.nombre = nombre
        producto.precio = precio
        producto.descripcion = descripcion
        producto.save()

        return redirect('listar_productos')

    return render(request, 'productos/editar.html', {'producto': producto})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    messages.success(request, 'Producto eliminado.')
    return redirect('listar_productos')
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView    

# Vista para marcar producto como completado
def marcar_completado(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.completado = not producto.completado
    producto.save()
    estado = 'completado' if producto.completado else 'desmarcado'
    messages.success(request, f'Producto {estado} exitosamente.')
    return redirect('listar_productos')


def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        Producto.objects.create(nombre=nombre, precio=precio, descripcion=descripcion)
        messages.success(request, 'Producto agregado exitosamente.')
        return redirect('listar_productos')
    return render(request, 'productos/agregar.html')
def completar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.completado = True
    producto.save()
    messages.success(request, 'Producto marcado como completado.')
    return redirect('listar_productos') 