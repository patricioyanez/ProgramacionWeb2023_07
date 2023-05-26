from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca= models.AutoField(primary_key=True) # se puede omitir. se crea solo
    nombre = models.CharField(max_length=50, null=False, unique=True, blank=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

#Pasos para migrar modelos personalizados:
#1.- Preparar migración
# py manage.py makemigrations crud

#2.- Realizar la migración
# py manage.py migrate crud

# crear modelo y crud para categoria, tipo de pago