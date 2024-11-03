from django.db.models import F, Sum
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
from django.db.models import Sum
# views.py


# Página de inicio

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    # Verifica si el producto ya existe en el carrito
    item, item_created = CarritoItem.objects.get_or_create(
        carrito=carrito, producto=producto)

    # Solo incrementa la cantidad si el item ya existía
    if not item_created:
        item.cantidad += 1
    else:
        item.cantidad = 1

    item.save()

    return redirect('carrito')


@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    items = carrito.carritoitem_set.all() if carrito else []

    # Calcula el total de todos los items en el carrito
    total_items = items.aggregate(total=Sum('cantidad'))['total'] or 0

    # Calcula el total para cada item y el total general del carrito
    for item in items:
        # Agrega el total de cada item al objeto
        item.total_item = item.cantidad * item.producto.precio

    # Suma de todos los items para el total del carrito
    total_carrito = sum(item.total_item for item in items)

    return render(request, 'carrito.html', {
        'items': items,
        'total_items': total_items,
        'total_carrito': total_carrito
    })


@login_required
def eliminar_producto_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)

    # Reduce la cantidad o elimina el item si la cantidad llega a 0
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()

    return redirect('carrito')


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
        messages.success(
            request, "¡Gracias por comprar con nosotros! Pronto recibirás un correo con la forma de pago y despacho oficial.")
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
    return render(request, 'panel_admin.html')

# Crear un nuevo producto


@login_required
def crear_producto(request):
    if request.method == 'POST':
        print(request.FILES)  # Agrega esta línea para depuración
        form = FormularioProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
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
            return redirect('lista_productos')
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
        return redirect('lista_productos')  # Redirigir a la lista de productos

    return render(request, 'confirmar_eliminacion.html', {'producto': producto})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def quienes_somos(request):
    return render(request, 'quienes_somos.html')
# Vista para cerrar sesión


def cerrar_sesion(request):
    logout(request)
    return redirect('base')


def base(request):
    return render(request, 'base.html')
