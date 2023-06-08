from django import forms
from django.forms import ModelForm

from .models import Categoria, Cliente

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields= "__all__" # todos los campos

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields= "__all__" # todos los campos
