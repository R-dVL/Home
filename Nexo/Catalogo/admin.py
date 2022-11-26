from django.contrib import admin
from .models import Libro, Pelicula, Serie

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "genero", "leido", "puntuacion")
    
@admin.register(Pelicula)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "genero", "vista", "puntuacion")
    
@admin.register(Serie)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "genero", "vista", "puntuacion")
