# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, OrdenEnvio

# Formulario de Registro de Usuario

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username' : 'Nombre de Usuario'}


# Formulario para Crear/Editar Producto
class FormularioProducto(forms.ModelForm):
    nombre = forms.CharField(label="Nombre del Producto")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    precio = forms.DecimalField(
        label="Precio", max_digits=10, decimal_places=2)
    stock = forms.IntegerField(label="Stock")
    imagen = forms.ImageField(
        label="Imagen", required=False)  # Campo de imagen

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock','imagen']  # Asegúrate de incluir 'imagen'

# Formulario para los Datos de Envío


class FormularioEnvio(forms.ModelForm):
    direccion = forms.CharField(label="Dirección")
    ciudad = forms.CharField(label="Ciudad")
    region = forms.CharField(label="Región")
    codigo_postal = forms.CharField(label="Código Postal")
    telefono = forms.CharField(label="Teléfono")
    email = forms.EmailField(label="Correo Electrónico")

    class Meta:
        model = OrdenEnvio
        fields = ['direccion', 'ciudad', 'region',
                'codigo_postal', 'telefono', 'email']
