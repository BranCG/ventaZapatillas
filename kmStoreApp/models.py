# kmStoreApp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def actualizar_stock(self):
        """Actualiza el stock basado en los movimientos"""
        from ControlStock.models import MovimientoStock  # Importación aquí para evitar importación circular
        total_movimientos = MovimientoStock.objects.filter(
            producto=self
        ).aggregate(total=Sum('cantidad'))['total'] or 0
        
        self.stock = total_movimientos
        self.save()
    
    def tiene_stock_suficiente(self, cantidad):
        """Verifica si hay suficiente stock para una cantidad dada"""
        return self.stock >= cantidad
    
    def necesita_reorden(self):
        """Verifica si el producto necesita ser reordenado"""
        try:
            config = self.configuracionstock
            return self.stock <= config.punto_reorden
        except ConfiguracionStock.DoesNotExist:
            return False
    
    def registrar_venta(self, cantidad, usuario):
        """Registra una venta y actualiza el stock"""
        from ControlStock.models import MovimientoStock
        if not self.tiene_stock_suficiente(cantidad):
            raise ValidationError('No hay suficiente stock disponible')
            
        MovimientoStock.objects.create(
            producto=self,
            cantidad=cantidad,
            tipo_movimiento='VENTA',
            usuario=usuario,
            nota='Venta realizada'
        )
    
    def registrar_entrada(self, cantidad, usuario, nota=''):
        """Registra una entrada de stock"""
        from ControlStock.models import MovimientoStock
        MovimientoStock.objects.create(
            producto=self,
            cantidad=cantidad,
            tipo_movimiento='ENTRADA',
            usuario=usuario,
            nota=nota
        )

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carritos_kmstore')
    productos = models.ManyToManyField(Producto, through='CarritoItem')

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class OrdenEnvio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordenes_kmstore')
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