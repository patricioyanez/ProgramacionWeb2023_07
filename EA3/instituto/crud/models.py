from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca= models.AutoField(primary_key=True) # se puede omitir. se crea solo
    nombre = models.CharField(max_length=50, null=False, unique=True, blank=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    idCategoria= models.AutoField(db_column='idCategoria', primary_key=True)
    nombre = models.CharField(max_length=50, unique=True, blank=False, null=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    idGenero= models.AutoField(db_column='idGenero', primary_key=True)
    nombre = models.CharField(max_length=20, unique=True, blank=False, null=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):    
    rut = models.IntegerField(primary_key=True, unique=True, null=False, blank=False)
    dv = models.CharField(max_length=1, null=False, blank=False, default="")
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=20, null=False, blank=False)
    genero = models.ForeignKey(Genero, db_column='idGenero', 
                                on_delete=models.CASCADE, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

#Pasos para migrar modelos personalizados:
#1.- Preparar migración
# py manage.py makemigrations crud

#2.- Realizar la migración
# py manage.py migrate crud

# crear modelo y crud para categoria, tipo de pago