from . import views
from django.urls import path

urlpatterns = [
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
]
# Ejercicios: Realizar el crud para categoria y genero
# Ejercicios: Crear Modelo de producto y migrar
# 127.0.0.1:8000/crud/marca