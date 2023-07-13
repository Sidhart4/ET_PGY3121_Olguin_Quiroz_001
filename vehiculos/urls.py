from django.urls import path
from vehiculos.views import * 

urlpatterns=[ 
    path('', index, name="index"),
    path('otra/', otra, name="otra"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/',mostrar, name="mostrar"),
    
    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]