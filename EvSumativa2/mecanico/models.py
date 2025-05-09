from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)


    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    descripction = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()