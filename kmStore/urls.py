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
    path('formularioDespacho/', views.formulario_despacho, name='formulario_despacho'),
    path('listaProductos/', views.lista_productos, name='listaProductos'),
    path('panelAdmin/', views.panel_admin, name='panel_admin'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/eliminar/<int:producto_id>/',views.eliminar_producto, name='eliminar_producto'),
    path('carrito/agregar/<int:producto_id>/',views.agregar_al_carrito, name='agregar_al_carrito'),
    path('producto/actualizar/<int:producto_id>/',views.actualizar_producto, name='actualizar_producto'),
    path('quienesSomos/', views.quienes_somos, name='quienesSomos'),
    path('cerrandoSesion/', views.cerrar_sesion, name='cerrarSesion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
