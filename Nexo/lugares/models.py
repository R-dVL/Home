from django.db import models
from django.contrib.gis.db.models import PointField
# Create your models here.

class Restaurante(models.Model):
    nombre = models.CharField(max_length = 50)
    tipo = models.CharField(max_length = 50)
    precio = models.IntegerField()
    lugar = models.CharField(max_length = 50)
    puntuacion = models.FloatField(blank = True, null = True)
    comentario = models.CharField(max_length = 500, blank = True, null = True)
    pendiente = models.BooleanField()
    ubicacion = PointField(blank = True, null = True)
    
    def __str__(self):
        return self.nombre