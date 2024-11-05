from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User #importo el modelo User que proporciona un sistema de autenticación predefinido.
from .models import Producto, OrdenEnvio


# Formulario para actualizar datos de usuarios.
class FormularioActualizacionCuenta(UserChangeForm): #Formulario proporcionado por Django para facilitar la edición de información de usuarios en el panel de administración.
    class Meta:
        model = User   #relacion con modelo user django
        fields = ['username', 'email']

# Formulario para registrar nuevos usuarios
class FormularioRegistro(UserCreationForm): #es un formulario de Django utilizado para crear nuevos usuarios de forma valida y segura.
    email = forms.EmailField(
        required=True, help_text='Requerido. Ingresa una dirección de correo electrónico válida.') #alerta para ingresar mail valido.

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Formulario para crear o editar productos
class FormularioProducto(forms.ModelForm): #Django crea automáticamente loss campos del formulario en función de los campos definidos en un modelo específico.
    nombre = forms.CharField(label="Nombre del Producto")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea) #campo de texto expandido.
    precio = forms.DecimalField(label="Precio", max_digits=10)
    stock = forms.IntegerField(label="Stock")
    imagen = forms.ImageField(label="Imagen", required=False)  # Campo de imagenn

    class Meta:
        model = Producto  #relacion con modelo producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']


# Formulario para ingresar los datos de envío de una orden
class FormularioEnvio(forms.ModelForm): #Django crea automáticamente los campos del formulario en función de los campos definidos en un modelo específico
    direccion = forms.CharField(label="Dirección")
    ciudad = forms.CharField(label="Ciudad")
    region = forms.CharField(label="Región")
    codigo_postal = forms.CharField(label="Código Postal")
    telefono = forms.CharField(label="Teléfono")
    email = forms.EmailField(label="Correo Electrónico")

    class Meta:
        model = OrdenEnvio
        fields = ['direccion', 'ciudad', 'region','codigo_postal', 'telefono', 'email']



