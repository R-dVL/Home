from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Libro, Pelicula, Serie

# Create your views here.
def pendientes(request):
    lista_libros = Libro.objects.order_by('-lectura')
    lista_pelis = Pelicula.objects.order_by('-visualizacion')
    lista_series = Serie.objects.order_by('-visualizacion')
    context = {
        'lista_libros': lista_libros,
        'lista_pelis': lista_pelis,
        'lista_series': lista_series,
        }
    return render(request, 'Catalogo/pendientes.html', context)

def libros(request):
    lista_libros = Libro.objects.order_by('-lectura')[:30]
    context = {'lista_libros': lista_libros}
    return render(request, 'Catalogo/libros.html', context)

def peliculas(request):
    lista_pelis = Pelicula.objects.order_by('-visualizacion')[:30]
    context = {'lista_pelis': lista_pelis}
    return render(request, 'Catalogo/peliculas.html', context)

def series(request):
    lista_series = Serie.objects.order_by('-visualizacion')[:30]
    context = {'lista_series': lista_series}
    return render(request, 'Catalogo/series.html', context)