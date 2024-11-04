"""
URL configuration for kmStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.base, name='base')
Class-based views
    1. Add an import:  from other_app.views import base
    2. Add a URL to urlpatterns:  path('', base.as_view(), name='base')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from kmStoreApp import views
from django.conf import settings

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
]


# Esta línea permite que Django sirva archivos de medios (como imágenes) en modo de desarrollo,
# verificando si DEBUG está activado y usando MEDIA_URL y MEDIA_ROOT para definir su acceso.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

