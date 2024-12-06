from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from kmStoreApp import views
from django.conf import settings
from ControlStock import views as stock_views
from kmBoletas.views import enviar_boleta_por_correo,crear_boleta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('producto/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('carrito/agregar/<int:producto_id>/',views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/',views.eliminar_producto_carrito, name='eliminar_producto_carrito'),
    path('formularioDespacho/', views.formulario_despacho, name='formulario_despacho'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/eliminar/<int:producto_id>/',views.eliminar_producto, name='eliminar_producto'),
    path('producto/actualizar/<int:producto_id>/',views.actualizar_producto, name='actualizar_producto'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('mi_cuenta/', views.modificar_cuenta, name='modificar_cuenta'),
    path('eliminar_cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),    
    # URLs de control de stock
    path('stock/reporte/', stock_views.reporte_stock, name='reporte_stock'),
    path('stock/movimientos/', stock_views.movimientos_stock, name='movimientos_stock'),
    path('stock/movimientos/<int:producto_id>/', stock_views.movimientos_producto, name='movimientos_producto'),
    path('stock/registrar-movimiento/<int:producto_id>/', stock_views.registrar_movimiento, name='registrar_movimiento'),
    #Boletas
    path('enviar-boleta/<int:boleta_id>/', enviar_boleta_por_correo, name='enviar_boleta'),
    path('crear-boleta',crear_boleta,name="crear_boleta"),
    path('API/',include('API.urls'))

]# Esta línea permite que Django sirva archivos de medios (como imágenes) en modo de desarrollo,
# verificando si DEBUG está activado y usando MEDIA_URL y MEDIA_ROOT para definir su acceso.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

