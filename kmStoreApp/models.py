from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.producto.nombre}"


class OrdenEnvio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"Orden de {self.usuario}"
