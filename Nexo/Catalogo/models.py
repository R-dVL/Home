from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length = 200)
    autor = models.CharField(max_length = 200)
    genero = models.CharField(max_length = 200)
    subgenero = models.CharField(max_length = 200)
    publicacion = models.DateField("Fecha de publicación")
    lectura = models.DateField("Fecha de lectura")
    puntuacion = models.FloatField()
    leido = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length = 200)
    director = models.CharField(max_length = 200)
    genero = models.CharField(max_length = 200)
    subgenero = models.CharField(max_length = 200)
    estreno = models.DateField("Fecha de estreno")
    visualizacion = models.DateField("Fecha de visualización")
    puntuacion = models.FloatField()
    vista = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
class Serie(models.Model):
    nombre = models.CharField(max_length = 200)
    director = models.CharField(max_length = 200)
    genero = models.CharField(max_length = 200)
    subgenero = models.CharField(max_length = 200)
    estreno = models.DateField("Fecha de estreno")
    visualizacion = models.DateField("Fecha de visualización")
    puntuacion = models.FloatField()
    vista = models.BooleanField()
    
    def __str__(self):
        return self.nombre