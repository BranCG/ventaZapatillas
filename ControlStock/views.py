from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from kmStoreApp.models import Producto
from .models import MovimientoStock, ConfiguracionStock

@login_required
def reporte_stock(request):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return redirect('lista_productos')
        
    productos = Producto.objects.all()
    productos_bajo_stock = [p for p in productos if p.necesita_reorden()]
    
    context = {
        'productos': productos,
        'productos_bajo_stock': productos_bajo_stock,
    }
    return render(request, 'lista_productos.html', context)

@login_required
def movimientos_stock(request):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return redirect('lista_productos')
        
    movimientos = MovimientoStock.objects.all().order_by('-fecha')
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'panel_admin.html', context)

@login_required
def movimientos_producto(request, producto_id):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return redirect('lista_productos')
        
    producto = get_object_or_404(Producto, id=producto_id)
    movimientos = MovimientoStock.objects.filter(
        producto=producto
    ).order_by('-fecha')
    
    context = {
        'producto': producto,
        'movimientos': movimientos,
    }
    return render(request, 'actualizar_producto.html', context)

@login_required
def registrar_movimiento(request, producto_id):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return redirect('lista_productos')
        
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        tipo = request.POST.get('tipo_movimiento')
        try:
            cantidad = int(request.POST.get('cantidad', 0))
            if cantidad <= 0:
                raise ValueError('La cantidad debe ser mayor a 0')
                
            nota = request.POST.get('nota', '')
            
            if tipo == 'ENTRADA':
                producto.registrar_entrada(cantidad, request.user, nota)
                messages.success(request, f'Se agregaron {cantidad} unidades al stock')
            elif tipo == 'SALIDA':
                if producto.tiene_stock_suficiente(cantidad):
                    MovimientoStock.objects.create(
                        producto=producto,
                        cantidad=-cantidad,
                        tipo_movimiento='SALIDA',
                        usuario=request.user,
                        nota=nota
                    )
                    messages.success(request, f'Se retiraron {cantidad} unidades del stock')
                else:
                    messages.error(request, 'No hay suficiente stock disponible')
            elif tipo == 'AJUSTE':
                MovimientoStock.objects.create(
                    producto=producto,
                    cantidad=cantidad,
                    tipo_movimiento='AJUSTE',
                    usuario=request.user,
                    nota=nota
                )
                messages.success(request, f'Stock ajustado a {cantidad} unidades')
                
            # Actualizar el stock del producto
            producto.actualizar_stock()
            
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f'Error al actualizar el stock: {str(e)}')
        
        # Redirigir a la lista de productos después de la actualización
        return redirect('lista_productos')
    
    return redirect('lista_productos')

    
@login_required
def reporte_stock(request):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return redirect('lista_productos')
    
    productos = Producto.objects.all()
    for producto in productos:
        ConfiguracionStock.objects.get_or_create(
            producto=producto,
            defaults={
                'stock_minimo': 5,
                'stock_maximo': 100,
                'punto_reorden': 10
            }
        )
    
    productos_bajo_stock = [p for p in productos if p.necesita_reorden()]
    
    context = {
        'productos': productos,
        'productos_bajo_stock': productos_bajo_stock,
    }
    return render(request, 'lista_productos.html', context)