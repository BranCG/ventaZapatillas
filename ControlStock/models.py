from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.utils import timezone

class MovimientoStock(models.Model):
    TIPO_MOVIMIENTO = (
        ('ENTRADA', 'Entrada de Stock'),
        ('SALIDA', 'Salida de Stock'),
        ('AJUSTE', 'Ajuste de Inventario'),
        ('VENTA', 'Venta'),
    )
    
    producto = models.ForeignKey('kmStoreApp.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movimientos_stock')
    nota = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.tipo_movimiento in ['SALIDA', 'VENTA']:
            self.cantidad = -abs(self.cantidad)
        elif self.tipo_movimiento == 'ENTRADA':
            self.cantidad = abs(self.cantidad)
            
        super().save(*args, **kwargs)
        
        self.producto.actualizar_stock()

class ConfiguracionStock(models.Model):
    producto = models.OneToOneField('kmStoreApp.Producto', on_delete=models.CASCADE)
    stock_minimo = models.PositiveIntegerField(default=5)
    stock_maximo = models.PositiveIntegerField(default=100)
    punto_reorden = models.PositiveIntegerField(default=10)
    
    def clean(self):
        if self.stock_minimo >= self.stock_maximo:
            raise ValidationError('El stock mínimo debe ser menor que el stock máximo')
        if self.punto_reorden <= self.stock_minimo:
            raise ValidationError('El punto de reorden debe ser mayor que el stock mínimo')

    def __str__(self):
        return f"Configuración de stock para {self.producto.nombre}"