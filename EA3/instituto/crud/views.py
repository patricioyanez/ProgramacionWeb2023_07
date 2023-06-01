from django.shortcuts import render
# importar modelos
from .models import Marca
# Create your views here.

def marca(request):
    return render(request, 'marca.html')