from django.contrib import admin
from .models import Libro, Pelicula, Serie

# Register your models here.
admin.site.register(Libro)
admin.site.register(Pelicula)
admin.site.register(Serie)