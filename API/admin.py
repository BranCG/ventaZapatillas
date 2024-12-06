from django.contrib import admin
from API.models import *

# Register your models here

class ProductoAdmin(admin.ModelAdmin):
    list_display=['id','nombre','precio','stock']

class CarritoAdmin(admin.ModelAdmin):
    list_display=['id','usuario_id']

class CarritoItemAdmin(admin.ModelAdmin):
    list_display=['id','cantidad','carrito_id','producto_id']

class OrdenEnvioAdmin(admin.ModelAdmin):
    list_display=['id','direccion','ciudad','region','codigo_postal','telefono','email','fecha_orden','completado','usuario_id']

class BoletaAdmin(admin.ModelAdmin):
    list_display=['id','numero_boleta','fecha_emision','total','cliente_id']

class DetalleBoletaAdmin(admin.ModelAdmin):
    list_display=['id','cantidad','subtotal','boleta_id','producto_id']

class MovimientoStockAdmin(admin.ModelAdmin):
    list_display=['id','cantidad','tipo_movmiento','fecha','nota','producto_id','usuario_id']

class ConfiguracionStockAdmin(admin.ModelAdmin):
    list_display=['id','stock_minimo','stock_maximo','producto_id']

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(CarritoItem,CarritoItemAdmin)
admin.site.register(OrdenEnvio,OrdenEnvioAdmin)
admin.site.register(Boleta,BoletaAdmin)
admin.site.register(DetalleBoleta,DetalleBoleta)
admin.site.register(MovimientoStock,MovimientoStockAdmin)
admin.site.register(ConfiguracionStock,ConfiguracionStockAdmin)