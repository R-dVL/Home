from django.urls import path, include
from . import views

urlpatterns = [
    path('pendientes/', views.pendientes, name = 'pendientes'),
    path('libros/', views.libros, name = "libros"),
    path('libros/<int:libro_id>/', views.libros_detalle, name="detalle"),
    path('peliculas/', views.peliculas, name = "peliculas"),
    path('series/', views.series, name = "series"),
]