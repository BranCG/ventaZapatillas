from django.contrib import admin
from .models import MovimientoStock, ConfiguracionStock

@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad', 'tipo_movimiento', 'fecha', 'usuario']
    list_filter = ['tipo_movimiento', 'fecha', 'usuario']
    search_fields = ['producto__nombre', 'nota']
    date_hierarchy = 'fecha'

@admin.register(ConfiguracionStock)
class ConfiguracionStockAdmin(admin.ModelAdmin):
    list_display = ['producto', 'stock_minimo', 'stock_maximo', 'punto_reorden']
    list_filter = ['stock_minimo', 'stock_maximo', 'punto_reorden']
    search_fields = ['producto__nombre']