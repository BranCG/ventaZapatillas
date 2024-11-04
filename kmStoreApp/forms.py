from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, OrdenEnvio

# Formulario para registrar nuevos usuarios


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text='Requerido. Ingresa una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Formulario para crear o editar productos
class FormularioProducto(forms.ModelForm):
    nombre = forms.CharField(label="Nombre del Producto")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    precio = forms.DecimalField(
        label="Precio", max_digits=10, decimal_places=2)
    stock = forms.IntegerField(label="Stock")
    imagen = forms.ImageField(
        label="Imagen", required=False)  #Campo de imagen

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock','imagen']


# Formulario para ingresar los datos de envío de una orden
class FormularioEnvio(forms.ModelForm):
    direccion = forms.CharField(label="Dirección")
    ciudad = forms.CharField(label="Ciudad")
    region = forms.CharField(label="Región")
    codigo_postal = forms.CharField(label="Código Postal")
    telefono = forms.CharField(label="Teléfono")
    email = forms.EmailField(label="Correo Electrónico")

    class Meta:
        model = OrdenEnvio
        fields = ['direccion', 'ciudad', 'region','codigo_postal', 'telefono', 'email']
