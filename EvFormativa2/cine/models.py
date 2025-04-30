from django.db import models

class Peliculas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10)
    duracion = models.IntegerField(max_length=3)

class SalaDeCine(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    tipoDeSala = models.CharField(max_length=50)
    
