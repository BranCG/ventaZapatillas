from django.contrib import admin
from .models import Producto, Carrito, CarritoItem, OrdenEnvio

# Register your models here.
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(OrdenEnvio)
#Aqui registra mis modelos en el sitio de administración de Django.
