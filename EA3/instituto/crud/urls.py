from . import views
from django.urls import path

urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('categoriaForm', views.categoriaForm, name='categoriaForm'),
    path('clienteForm', views.clienteForm, name='clienteForm'),
]
# Ejercicios: Realizar el crud para categoria y genero
# Ejercicios: Crear Modelo de producto y migrar
# 127.0.0.1:8000/crud/marca