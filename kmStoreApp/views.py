from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Producto, Carrito, CarritoItem
from .forms import FormularioProducto, FormularioRegistro, FormularioEnvio, FormularioActualizacionCuenta


# Vista para iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel_admin') if user.is_staff else redirect('base')
        messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')


# Vista para registrar nuevos usuarios
def registrar_usuario(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('base')
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})


# Cierra la sesión del usuario
def cerrar_sesion(request):
    logout(request)
    return redirect('base')


# Muestra la sección "Quiénes Somos"
def quienes_somos(request):
    return render(request, 'quienes_somos.html')


# Vista del Panel de Administración
@login_required
@user_passes_test(lambda u: u.is_staff)
def panel_admin(request):
    return render(request, 'panel_admin.html')


# Lista todos los productos disponibles
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


# Crea un nuevo producto
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = FormularioProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto creado con éxito!')
            return redirect('lista_productos')
    else:
        form = FormularioProducto()
    return render(request, 'crear_producto.html', {'form': form})


# Modifica un producto existente
@login_required
@user_passes_test(lambda u: u.is_staff)
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = FormularioProducto(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto actualizado con éxito!')
            return redirect('lista_productos')
    else:
        form = FormularioProducto(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form, 'producto': producto})


# Elimina un producto existente
@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        producto.delete()
        messages.success(request, '¡Producto eliminado con éxito!')
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminacion.html', {'producto': producto})


# Agrega un producto al carrito del usuario o actualiza la cantidad si ya existe
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, item_creado = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad = item.cantidad + 1 if not item_creado else 1
    item.save()
    return redirect('carrito')


# Muestra el carrito del usuario con detalles de los artículos y totales
@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    items = carrito.carritoitem_set.all() if carrito else []
    
    total_items = items.aggregate(total=Sum('cantidad'))['total'] or 0
    for item in items:
        item.total_item = item.cantidad * item.producto.precio
    total_carrito = sum(item.total_item for item in items)

    return render(request, 'carrito.html', {
        'items': items,
        'total_items': total_items,
        'total_carrito': total_carrito
    })


# Elimina un producto del carrito o disminuye su cantidad
@login_required
def eliminar_producto_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()
    return redirect('carrito')


# Muestra los detalles de un producto específico
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})


# Formulario para ingresar los datos de envío
@login_required
def formulario_despacho(request):
    if request.method == "POST":
        formulario = FormularioEnvio(request.POST)
        if formulario.is_valid():
            orden = formulario.save(commit=False)
            orden.usuario = request.user
            orden.save()
            messages.success(request, "¡GRACIAS POR PREFERIRNOS! Pronto recibirás un correo para elegir tu talla y forma de pago.")
            return redirect('base')
    else:
        formulario = FormularioEnvio()
    return render(request, 'formulario_despacho.html', {'formulario': formulario})


# Muestra la página base
def base(request):
    return render(request, 'base.html')


# Vista para modificar datos del usuario
@login_required
def modificar_cuenta(request):
    if request.method == 'POST':
        user_form = FormularioActualizacionCuenta(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, '¡Tus datos han sido actualizados con éxito!.')
            return redirect('base')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        user_form = FormularioActualizacionCuenta(instance=request.user)
    return render(request, 'modificar_cuenta.html', {'user_form': user_form})


# Vista para eliminar cuenta de usuarioz
@login_required
def eliminar_cuenta(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
        return redirect('base')
    return redirect('modificar_cuenta')
