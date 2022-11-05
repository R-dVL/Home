from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('libros/', views.libros, name = "libros"),
    path('peliculas/', views.peliculas, name = "peliculas"),
    path('series/', views.series, name = "series"),
]