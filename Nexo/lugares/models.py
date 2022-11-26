from django.db import models

# Create your models here.

class Restaurante(models.Model):
    nombre = models.CharField(max_length = 50)
    tipo = models.CharField(max_length = 50)
    precio = models.IntegerField()
    lugar = models.CharField(max_length = 50)
    puntuacion = models.FloatField(blank = True, null = True)
    comentario = models.CharField(max_length = 500, blank = True, null = True)
    pendiente = models.BooleanField()
    
    def __str__(self):
        return self.nombre