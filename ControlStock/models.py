from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MovimientoStock(models.Model):
    TIPO_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('VENTA', 'Venta')
    ]
    
    producto = models.ForeignKey('kmStoreApp.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.TextField(blank=True, null=True)

    def actualizar_cantidad(self):
        if self.tipo_movimiento in ['SALIDA', 'VENTA']:
            self.cantidad = -abs(self.cantidad)
        super().save()
        self.producto.actualizar_stock()

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.producto.nombre} - {self.cantidad}"

class ConfiguracionStock(models.Model):
    producto = models.OneToOneField('kmStoreApp.Producto', on_delete=models.CASCADE)
    stock_minimo = models.PositiveIntegerField(default=5)
    stock_maximo = models.PositiveIntegerField(default=100)
    
    def validar_stock(self):
        if self.stock_minimo >= self.stock_maximo:
            raise ValidationError('El stock mínimo debe ser menor que el stock máximo')

    def __str__(self):
        return f"Config. stock: {self.producto.nombre}"