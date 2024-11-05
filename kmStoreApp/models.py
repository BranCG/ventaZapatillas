from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Modelo para representar los productos disponibles en la tienda
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10 , decimal_places=2) #especificaa el número total de dígitos que se pueden almacenar
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True) # uploadindica la carpeta en la que se almacenarán las imágenes subidas. blank no requerido, nulo para default imagen.

    def __str__(self):
        return self.nombre


# Modelo para representar el carrito de compras de un usuario
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # especifica lo que sucede cuando el usuario relacionado es eliminado. CASCADE indica que si el usuario se elimina, todos los carritos asociados con él también se eliminarán automáticamente.
    productos = models.ManyToManyField(Producto, through='CarritoItem') #Este parámetro indica que la relación de muchos a muchos entre Carrito y Producto se gestionará a través de un modelo intermedio llamado CarritoItem. 


# Modelo para representar los artículos dentro del carrito de un usuario
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)


# Modelo para representar la orden de envío de un usuario
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
