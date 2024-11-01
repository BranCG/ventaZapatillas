"""
URL configuration for kmStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from kmStoreApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.register_view, name='registro'),
    path('producto/', views.producto_detail, name='detalle_producto'),
    path('carrito/', views.carrito_view, name='carrito'),
    path('formularioDespacho/', views.checkout_view, name='formulario_despacho'),
    path('panelAdmin/', views.admin_dashboard, name='panel_admin'),
    path('producto/crear/', views.producto_create, name='crear_producto'),
    path('producto/modificar/', views.producto_update, name='actualizar_producto'),
    path('producto/eliminar/',views.producto_delete, name='eliminar_producto'),
]
