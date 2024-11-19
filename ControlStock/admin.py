from django.contrib import admin
from .models import MovimientoStock, ConfiguracionStock

@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = ['producto', 'tipo_movimiento', 'cantidad', 'fecha', 'usuario']
    list_filter = ['tipo_movimiento', 'fecha', 'usuario']
    search_fields = ['producto__nombre', 'nota']
    date_hierarchy = 'fecha'
    readonly_fields = ['fecha']
    list_per_page = 20

@admin.register(ConfiguracionStock)
class ConfiguracionStockAdmin(admin.ModelAdmin):
    list_display = ['producto', 'stock_minimo', 'stock_maximo']
    list_filter = ['stock_minimo', 'stock_maximo']
    search_fields = ['producto__nombre']
    list_per_page = 20

