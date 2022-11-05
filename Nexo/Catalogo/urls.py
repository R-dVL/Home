from django.urls import path, include
from . import views

urlpatterns = [
    path('pendientes/', views.pendientes, name = 'pendientes'),
    path('libros/', views.libros, name = "libros"),
    path('peliculas/', views.peliculas, name = "peliculas"),
    path('series/', views.series, name = "series"),
]