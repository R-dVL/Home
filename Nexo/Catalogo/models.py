from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 50)
    genero = models.CharField(max_length = 50)
    subgenero = models.CharField(max_length = 50, blank = True, null = True)
    publicacion = models.DateField("Fecha de publicación")
    leido = models.BooleanField()
    lectura = models.DateField("Fecha de lectura", blank = True, null = True)
    puntuacion = models.FloatField(blank = True, null = True)
    portada = models.ImageField(upload_to="portadas", height_field=None, width_field=None, max_length=100, blank = True, null = True)
    comentario = models.CharField(max_length = 200, blank = True, null = True)
    
    def __str__(self):
        return self.nombre
    
# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length = 200)
    director = models.CharField(max_length = 200)
    genero = models.CharField(max_length = 200)
    subgenero = models.CharField(max_length = 200, blank = True, null = True)
    estreno = models.DateField("Fecha de estreno")
    visualizacion = models.DateField("Fecha de visualización", blank = True, null = True)
    puntuacion = models.FloatField(blank = True, null = True)
    vista = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
class Serie(models.Model):
    nombre = models.CharField(max_length = 200)
    director = models.CharField(max_length = 200)
    genero = models.CharField(max_length = 200)
    subgenero = models.CharField(max_length = 200, blank = True, null = True)
    estreno = models.DateField("Fecha de estreno")
    visualizacion = models.DateField("Fecha de visualización", blank = True, null = True)
    puntuacion = models.FloatField(blank = True, null = True)
    vista = models.BooleanField()
    
    def __str__(self):
        return self.nombre