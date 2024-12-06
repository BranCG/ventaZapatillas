from rest_framework import serializers
from API.models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrito
        fields='__all__'


class CarritoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarritoItem
        fields='__all__'

class OrdenDeEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrdenEnvio
        filds='__all___'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Boleta
        fields='__all__'

class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleBoleta
        fields='__all__'

class MovimientosStockSerializer(serializers.ModelSerializer):
    class Meta:
        model=MovimientoStock
        fields='__all__'

class ConfiguracionStockSerilizer(serializers.ModelSerializer):
    class Meta:
        model=ConfiguracionStock
        fields='__all__'