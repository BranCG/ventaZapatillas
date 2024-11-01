from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, OrdenEnvio, CarritoItem
# Formularios personalizados
from .forms import FormularioProducto, FormularioRegistro, FormularioEnvio

# Página de inicio



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listaProductos.html', {'productos': productos})


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalleProducto.html', {'producto': producto})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, created = CarritoItem.objects.get_or_create(
        carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')


@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, 'carrito.html', {'items': items})

def home(request):
    return render(request, 'base.html')

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})

# Vista para iniciar sesión


def iniciar_sesion(request):
    if request.method == "POST":
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')
        usuario = authenticate(
            request, username=nombre_usuario, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

# Vista para registrar usuarios


def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('iniciar_sesion')
    else:
        formulario = FormularioRegistro()
    return render(request, 'registro.html', {'formulario': formulario})

# Vista de detalle de un producto


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})


# Formulario para ingresar los datos de despacho


@login_required
def formulario_despacho(request):
    if request.method == "POST":
        formulario = FormularioEnvio(request.POST)
        if formulario.is_valid():
            orden = formulario.save(commit=False)
            orden.usuario = request.user
            orden.save()
            return redirect('carrito')
    else:
        formulario = FormularioEnvio()
    return render(request, 'formulario_despacho.html', {'formulario': formulario})

# Panel de administración para el CRUD de productos


@login_required
def panel_admin(request):
    productos = Producto.objects.all()
    return render(request, 'panelAdmin.html', {'productos': productos})

# Crear un nuevo producto


@login_required
def crear_producto(request):
    if request.method == "POST":
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('panel_administracion')
    else:
        formulario = FormularioProducto()
    return render(request, 'crear_producto.html', {'formulario': formulario})

# Modificar un producto existente


@login_required
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        formulario = FormularioProducto(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('panel_administracion')
    else:
        formulario = FormularioProducto(instance=producto)
    return render(request, '/actualizar_producto.html', {'formulario': formulario})

# Eliminar un producto existente


@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect('panel_administracion')
    return render(request, 'eliminar_producto.html', {'producto': producto})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listaProductos.html', {'productos': productos})
