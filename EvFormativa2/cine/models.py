from django.db import models
from datetime import timedelta

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
    fecha_hora_termino = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # Calculate the end time based on the movie duration
        self.fecha_hora_termino = self.fecha_hora_inicio + timedelta(minutes=self.pelicula.duracion)

        # Check for overlapping functions in the same sala
        overlapping_funciones = Funcion.objects.filter(
            sala=self.sala,
            fecha_hora_inicio__lt=self.fecha_hora_termino,
            fecha_hora_termino__gt=self.fecha_hora_inicio
        ).exclude(id=self.id)

        if overlapping_funciones.exists():
            raise ValueError("Ya existe una función en este horario en la misma sala.")

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('sala', 'fecha_hora_inicio')

    
