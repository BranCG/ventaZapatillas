from .models import Producto
from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, OrdenEnvio, CarritoItem
# Formularios personalizados
from .forms import FormularioProducto, RegistroUsuarioForm, FormularioEnvio
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import FormularioProducto

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
    return redirect('agregar_al_carrito')


@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, 'carrito.html', {'items': items})



# Vista de inicio de sesión


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página del panel de administración si el usuario es staff
            if user.is_staff:
                return redirect('panel_admin')
            else:
                return redirect('base')
        else:
            messages.error(
                request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')

# Vista para registrar usuarios


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Iniciar sesión automáticamente después del registro
            login(request, usuario)
            # Cambia 'home' a la vista a la que quieras redirigir
            return redirect('base')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

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


# Vista del Panel Admin
@login_required
# Restringe el acceso a usuarios que son staff
@user_passes_test(lambda u: u.is_staff)
def panel_admin(request):
    # Lógica del panel de administración
    return render(request, 'panelAdmin.html')

# Crear un nuevo producto


@login_required
def crear_producto(request):
    if request.method == 'POST':
        print(request.FILES)  # Agrega esta línea para depuración
        form = FormularioProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listaProductos')
    else:
        form = FormularioProducto()

    return render(request, 'crear_producto.html', {'form': form})


# Modificar un producto existente
@login_required
@user_passes_test(lambda u: u.is_staff)
def actualizar_producto(request, producto_id):
    # Obtiene el producto a actualizar
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        # Pasa la instancia del producto
        form = FormularioProducto(
            request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()  # Guarda los cambios
            # Redirige a la lista de productos
            return redirect('listaProductos')
    else:
        # Crea el formulario con la instancia existente
        form = FormularioProducto(instance=producto)

    return render(request, 'actualizar_producto.html', {'form': form, 'producto': producto})

# Eliminar un producto existente


@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == "POST":
        producto.delete()
        return redirect('listaProductos')  # Redirigir a la lista de productos

    return render(request, 'confirmar_eliminacion.html', {'producto': producto})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listaProductos.html', {'productos': productos})


def quienes_somos(request):
    return render(request, 'quienesSomos.html')
# Vista para cerrar sesión

def cerrar_sesion(request):
    logout(request)
    return redirect('base')

def base(request):
    return render(request, 'base.html')

