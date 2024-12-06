from API import views
from django.urls import path
from django.contrib import admin

urlpatterns =[
    path('producto/',views.ProductoList.as_view()),
    path('producto/<int:pk>',views.ProductoDetalle.as_view()),
    path('carrito/',views.CarritoList.as_view()),
    path('carrito/<int:pk>',views.CarritoDetalle.as_view()),
    path('carritoItem/',views.CarritoItemList.as_view()),
    path('carritoItem/<int:pk>',views.CarritoItemDetalle.as_view()),
    path('ordenEnvio/',views.ordenEnvioList.as_view()),
    path('ordenEnvio/<int:pk>',views.ordenEnvioDetalle.as_view()),
    path('boleta/',views.boletaList.as_view()),
    path('boleta/<int:pk>',views.detalleBoletaDetalle.as_view()),
    path('detalleBoleta/',views.detalleBoletaList.as_view()),
    path('detalleBoelta/<int:pk>',views.detalleBoletaDetalle.as_view()),
    path('moviemientoStock/',views.movimientosStockList.as_view()),
    path('moviemientoStock/<int:pk>',views.movimientoStockDetalle.as_view()),
    path('configuracionStock/',views.configuracionStokList.as_view()),
    path('configuracionStock/<int:pk>',views.configuracionStockDetalle.as_view()),
    ]