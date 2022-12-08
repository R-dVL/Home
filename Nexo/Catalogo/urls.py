from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('pendientes/', views.pendientes, name = 'pendientes'),
    path('libros/', views.libros, name = "libros"),
    path('libros/<int:libro_id>/', views.libros_detalle, name="librosDetalle"),
    path('peliculas/', views.peliculas, name = "peliculas"),
    path('peliculas/<int:pelicula_id>/', views.peliculas_detalle, name="peliculasDetalle"),
    path('series/', views.series, name = "series"),
    path('series/<int:serie_id>/', views.series_detalle, name="seriesDetalle"),
]