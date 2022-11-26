from django.contrib.gis import admin
from .models import Restaurante
# Register your models here.

@admin.register(Restaurante)
class RestauranteAdmin(admin.OSMGeoAdmin):
    list_display = ("nombre", "tipo", "precio", "puntuacion")

