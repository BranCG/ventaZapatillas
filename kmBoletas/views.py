from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .correo import Correo# Create your views here.
import uuid
from django.contrib import messages
from django.http import JsonResponse # type: ignore
from django.utils.timezone import now # type: ignore
from .models import Boleta, DetalleBoleta
from kmStoreApp.models import Carrito, CarritoItem
from django.template.loader import render_to_string# type: ignore
from django.utils.html import strip_tags# type: ignore

def crear_boleta(request):
    # Obtener el carrito del usuario
    carrito = Carrito.objects.filter(usuario=request.user).first()
    items = carrito.carritoitem_set.all() if carrito else []

    if not items.exists():
        return JsonResponse({'error': 'El carrito está vacío.'}, status=400)

    # Crear la boleta
    numero_boleta = str(uuid.uuid4()).split('-')[0]  # Número de boleta único
    boleta = Boleta.objects.create(
        numero_boleta=numero_boleta,
        cliente=request.user,
        fecha_emision=now(),
    )

    # Crear los detalles de la boleta
    
    for item in items:
        DetalleBoleta.objects.create(
            boleta=boleta,
            producto=item.producto,
            cantidad=item.cantidad,
            subtotal=item.cantidad * item.producto.precio
        )

    # Calcular el total de la boleta
    boleta.calcular_total()

    # Vaciar el carrito
    items.delete()
    enviar_boleta_por_correo(request, boleta.id)
    messages.success(request, "Gracias por preferirnos, revisa tu email para ver tu boleta.")
    return redirect('base')


def enviar_boleta_por_correo(request, boleta_id):
    # Obtener la boleta
    boleta = get_object_or_404(Boleta, id=boleta_id, cliente=request.user)

    # Renderizar la plantilla HTML
    html_content = render_to_string('boleta.html', {'boleta': boleta})
    text_content = strip_tags(html_content)  # Extraer texto plano para compatibilidad

    # Configurar el correo
    subject=f"Boleta #{boleta.numero_boleta}"
    body =text_content
    from_email='comercio@buscadoriaestudio.com'
    to= boleta.cliente.email
    
    # Enviar el correo
    notificador = Correo('comercio@buscadoriaestudio.com', '123Momiaes!', 'smtp.titan.email', 465)
    if notificador.enviar([to], subject, html_content, from_email,True):
        messages.success(request, 'Correo enviado exitosamente.')
    else:
        messages.error(request, 'Hubo un problema al enviar el correo.'+' ')
    notificador.cerrar()
    return redirect('base')
