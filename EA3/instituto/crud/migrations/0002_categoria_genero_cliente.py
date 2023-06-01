# Generated by Django 4.2.1 on 2023-05-31 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('dv', models.CharField(default='', max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('fechaNacimiento', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='crud.genero')),
            ],
        ),
    ]