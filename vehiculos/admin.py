from django.contrib import admin
from .models import Categoria, Vehiculo,detalle_boleta,Boleta

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)