from django.urls import path, include
from . import views

urlpatterns = [
    path('restaurantes/', views.restaurantes, name = 'restaurantes'),
]