from django.urls import path, include
from . import views
from lugares.views import Mapa, Restaurante

urlpatterns = [
    path('mapa/', Mapa.as_view()),
    path('restaurantes/', views.restaurantes, name = 'restaurantes'),
]