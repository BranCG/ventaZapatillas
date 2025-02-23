from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from .permissions import IsBrandon
from django.http import Http404

from django.http import HttpResponse

@login_required
def api_home(request):
    return HttpResponse("Bienvenido a la API")
# Create your views here.

class ProductoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self,request):
        productos=Producto.objects.all()
        serializer=ProductoSerializer(productos,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class ProductoDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get_object(self,pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        producto=self.get_object(pk)
        serializer=ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self,request,pk):
        producto=self.get_object(pk)
        serializer=ProductoSerializer(producto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        producto=self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CarritoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    def get(self,request):
        carrito=Carrito.objects.all()
        serializer=CarritoSerializer(carrito,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CarritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CarritoDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    def get_object(self,pk):
        try:
            return Carrito.objects.get(pk=pk)
        except Carrito.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        carrito=self.get_object(pk)
        serializer=CarritoSerializer(carrito)
        return Response(serializer.data)
    
    def put(self,request,pk):
        producto=self.get_object(pk)
        serializer=ProductoSerializer(producto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        carrito=self.get_object(pk)
        carrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CarritoItemList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    permission_classes = [IsBrandon]
    queryset = CarritoItem.objects.all()
    serializer_class = CarritoItemSerializer
    def get(self,request):
        carritoItem=CarritoItem.objects.all()
        serializer=CarritoItemSerializer(carritoItem,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CarritoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class CarritoItemDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = CarritoItem.objects.all()
    serializer_class = CarritoItemSerializer
    def get_object(self,pk):
        try:
            return CarritoItem.objects.get(pk=pk)
        except CarritoItem.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        carritoItem=self.get_object(pk)
        serializer=CarritoItemSerializer(carritoItem)
        return Response(serializer.data)
    
    def put(self,request,pk):
        carritoItem=self.get_object(pk)
        serializer=CarritoItemSerializer(carritoItem,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        carritoItem=self.get_object(pk)
        carritoItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ordenEnvioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = OrdenEnvio.objects.all()
    serializer_class = OrdenDeEnvioSerializer
    def get(self,request):
        ordenEnvio=OrdenEnvio.objects.all()
        serializer=OrdenDeEnvioSerializer(ordenEnvio,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=OrdenDeEnvioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ordenEnvioDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = OrdenEnvio.objects.all()
    serializer_class = OrdenDeEnvioSerializer
    def get_object(self,pk):
        try:
            return OrdenEnvio.objects.get(pk=pk)
        except OrdenEnvio.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        ordenEnvio=self.get_object(pk)
        serializer=OrdenDeEnvioSerializer(ordenEnvio)
        return Response(serializer.data)
    
    def put(self,request,pk):
        ordenEnvio=self.get_object(pk)
        serializer=OrdenDeEnvioSerializer(ordenEnvio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        ordenEnvio=self.get_object(pk)
        ordenEnvio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class boletaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    def get(self,request):
        boleta=Boleta.objects.all()
        serializer=BoletaSerializer(boleta,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BoletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class boletaDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    def get_object(self,pk):
        try:
            return Boleta.objects.get(pk=pk)
        except Boleta.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        ordenEnvio=self.get_object(pk)
        serializer=BoletaSerializer(ordenEnvio)
        return Response(serializer.data)
    
    def put(self,request,pk):
        boleta=self.get_object(pk)
        serializer=BoletaSerializer(boleta,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        boleta=self.get_object(pk)
        boleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class detalleBoletaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = DetalleBoleta.objects.all()
    serializer_class = DetalleBoletaSerializer
    def get(self,request):
        boletaDetalle=DetalleBoleta.objects.all()
        serializer=DetalleBoletaSerializer(boletaDetalle,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=DetalleBoletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class detalleBoletaDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = DetalleBoleta.objects.all()
    serializer_class = DetalleBoletaSerializer
    def get_object(self,pk):
        try:
            return DetalleBoleta.objects.get(pk=pk)
        except DetalleBoleta.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        ordenEnvio=self.get_object(pk)
        serializer=DetalleBoletaSerializer(ordenEnvio)
        return Response(serializer.data)
    
    def put(self,request,pk):
        ordenEnvio=self.get_object(pk)
        serializer=DetalleBoletaSerializer(ordenEnvio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        detalleBoleta=self.get_object(pk)
        detalleBoleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class movimientosStockList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = MovimientoStock.objects.all()
    serializer_class = MovimientosStockSerializer
    def get(self,request):
        movimientoStock=MovimientoStock.objects.all()
        serializer=MovimientosStockSerializer(movimientoStock,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=MovimientosStockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class movimientoStockDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = MovimientoStock.objects.all()
    serializer_class = MovimientosStockSerializer
    def get_object(self,pk):
        try:
            return MovimientoStock.objects.get(pk=pk)
        except MovimientoStock.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        movimientoStock=self.get_object(pk)
        serializer=MovimientosStockSerializer(movimientoStock)
        return Response(serializer.data)
    
    def put(self,request,pk):
        ordenEnvio=self.get_object(pk)
        serializer=MovimientosStockSerializer(ordenEnvio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        movimientoStock=self.get_object(pk)
        movimientoStock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class configuracionStokList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = ConfiguracionStock.objects.all()
    serializer_class = ConfiguracionStockSerilizer
    def get(self,request):
        confi=ConfiguracionStock.objects.all()
        serializer=ConfiguracionStockSerilizer(confi,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ConfiguracionStockSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class configuracionStockDetalle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsBrandon]
    queryset = ConfiguracionStock.objects.all()
    serializer_class = ConfiguracionStockSerilizer
    def get_object(self,pk):
        try:
            return ConfiguracionStock.objects.get(pk=pk)
        except ConfiguracionStock.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        confi=self.get_object(pk)
        serializer=ConfiguracionStockSerilizer(confi)
        return Response(serializer.data)
    
    def put(self,request,pk):
        confi=self.get_object(pk)
        serializer=ConfiguracionStockSerilizer(confi,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        confi=self.get_object(pk)
        confi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
