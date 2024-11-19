from django.db import models
from kmStoreApp.models import Producto
# from ControlStock.models import 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum

class Boleta(models.Model):
    numero_boleta = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boletas')
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Boleta #{self.numero_boleta} - {self.cliente.nombre}"

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.boleta}"