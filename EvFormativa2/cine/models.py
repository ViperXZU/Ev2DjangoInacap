from django.db import models

class Peliculas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10)
    duracion = models.IntegerField(max_length=3)

class SalaDeCine(models.Model):
    TIPO_SALA_CHOICES = [
        ('2D', '2D'),
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
        ('4DX', '4DX'),
    ]


    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField(max_length=3)
    tipoDeSala = models.CharField(max_length=50,
                                  choices=TIPO_SALA_CHOICES,
                                  default='2D'
                                  )
    
class Funcion(models.Model):
    id = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    sala = models.ForeignKey(SalaDeCine, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    

    
