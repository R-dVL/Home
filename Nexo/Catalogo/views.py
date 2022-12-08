from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Libro, Pelicula, Serie

# Create your views here.
def index(request):
    return render(request, 'Catalogo/index.html')
    
@login_required
def pendientes(request):
    lista_libros = Libro.objects.order_by('-autor')
    lista_pelis = Pelicula.objects.order_by('-director')
    lista_series = Serie.objects.order_by('-director')
    context = {
        'lista_libros': lista_libros,
        'lista_pelis': lista_pelis,
        'lista_series': lista_series,
        }
    return render(request, 'Catalogo/pendientes.html', context)

@login_required
def libros(request):
    lista_libros = Libro.objects.order_by('-puntuacion')[:30]
    context = {'lista_libros': lista_libros}
    return render(request, 'Catalogo/libros.html', context)

@login_required
def libros_detalle(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'Catalogo/librosDetalle.html', {'libro': libro})

@login_required
def peliculas(request):
    lista_pelis = Pelicula.objects.order_by('-puntuacion')[:30]
    context = {'lista_pelis': lista_pelis}
    return render(request, 'Catalogo/peliculas.html', context)

@login_required
def peliculas_detalle(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    return render(request, 'Catalogo/peliculasDetalle.html', {'pelicula': pelicula})

@login_required
def series(request):
    lista_series = Serie.objects.order_by('-puntuacion')[:30]
    context = {'lista_series': lista_series}
    return render(request, 'Catalogo/series.html', context)

@login_required
def series_detalle(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    return render(request, 'Catalogo/seriesDetalle.html', {'serie': serie})