from django.shortcuts import render
# importar modelos
from .models import Marca, Categoria
# Create your views here.

def categoria(request):
    context = {}
    if request.method == 'POST': # si hay solicitud POST
        id = int("0" + request.POST['id']) # convierte en numero
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST # checkeado es True, False si no

        if 'Grabar' in request.POST:
            if id == 0: #insert
                Categoria.objects.create(nombre=nombre, activo=activo)
                context = {'exito': 'Los datos fueron guardados'}
            else:
                try:
                    item = Categoria.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito': 'Los datos fueron modificados'}
                except:
                    context = {'error': 'No se pudo encontrar el registro'}

        elif 'Listar' in request.POST:
            listado = Categoria.objects.all() # select * from categoria
            context = {'listado': listado}

        elif 'Buscar' in request.POST:
            try: # select * from categoria where idcategoria = X
                item = Categoria.objects.get(pk = id) # 1 fila de la tabla 
                context = {'item': item }
            except:
                context = {'error': 'No se pudo encontrar el registro'}
        elif 'Eliminar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id) # 1 fila de la tabla 
                item.delete() # delete
                context = {'exito': 'El id fue eliminado'}
            except:
                context = {'error': 'No se pudo encontrar el registro'}


    return render(request, 'categoria.html', context)

def marca(request):
    context = {}
    if request.method == 'POST': # si hay solicitud POST
        id = int("0" + request.POST['id']) # convierte en numero
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST # checkeado es True, False si no

        if 'Grabar' in request.POST:
            if id == 0: #insert
                Marca.objects.create(nombre=nombre, activo=activo)
                context = {'exito': 'Los datos fueron guardados'}
            else:
                try:
                    item = Marca.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito': 'Los datos fueron modificados'}
                except:
                    context = {'error': 'No se pudo encontrar el registro'}

        elif 'Listar' in request.POST:
            listado = Marca.objects.all() # select * from marca
            context = {'listado': listado}

        elif 'Buscar' in request.POST:
            try: # select * from marca where idMarca = X
                item = Marca.objects.get(pk = id) # 1 fila de la tabla 
                context = {'item': item }
            except:
                context = {'error': 'No se pudo encontrar el registro'}
        elif 'Eliminar' in request.POST:
            try:
                item = Marca.objects.get(pk = id) # 1 fila de la tabla 
                item.delete() # delete
                context = {'exito': 'El id fue eliminado'}
            except:
                context = {'error': 'No se pudo encontrar el registro'}


    return render(request, 'marca.html', context)