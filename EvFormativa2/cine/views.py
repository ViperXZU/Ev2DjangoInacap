from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Peliculas, SalaDeCine
from .forms import PeliculasForm, SalaDeCineForm
import random

def peliculas_bulk_create(request):
    if Peliculas.objects.exists():
        return render(request, 'bulk_create_result.html', {'message': 'Los datos ya existen en la base de datos.'})

    nombres = ['El Gran Escape', 'La Aventura Espacial', 'Amor en Tiempos Modernos', 'El Misterio del Bosque']
    generos = ['Acción', 'Ciencia Ficción', 'Romance', 'Suspenso']
    clasificaciones = ['A', 'B', 'C']
    duraciones = [120, 150, 90, 110]

    peliculas = [
        Peliculas(
            nombre=random.choice(nombres),
            genero=random.choice(generos),
            clasificacion=random.choice(clasificaciones),
            duracion=random.choice(duraciones)
        )
        for _ in range(10)
    ]

    Peliculas.objects.bulk_create(peliculas)
    return HttpResponse('Datos creados correctamente.')

def peliculas_list(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas_list.html', {'peliculas': peliculas})

def peliculas_create(request):
    if request.method == 'POST':
        form = PeliculasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peliculas_list')
    else:
        form = PeliculasForm()
    return render(request, 'peliculas_form.html', {'form': form})

def peliculas_update(request, pk):
    pelicula = Peliculas.objects.get(pk=pk)
    if request.method == 'POST':
        form = PeliculasForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('peliculas_list')
    else:
        form = PeliculasForm(instance=pelicula)
    return render(request, 'peliculas_form.html', {'form': form})

def peliculas_delete(request, pk):
    pelicula = Peliculas.objects.get(pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('peliculas_list')
    return render(request, 'peliculas_delete.html', {'pelicula': pelicula})

def sala_de_cine_list(request):
    salas = SalaDeCine.objects.all()
    return render(request, 'sala_de_cine_list.html', {'salas': salas})

def sala_de_cine_create(request):
    if request.method == 'POST':
        form = SalaDeCineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sala_de_cine_list')
    else:
        form = SalaDeCineForm()
    return render(request, 'sala_de_cine_form.html', {'form': form})

def sala_de_cine_update(request, pk):
    sala = SalaDeCine.objects.get(pk=pk)
    if request.method == 'POST':
        form = SalaDeCineForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('sala_de_cine_list')
    else:
        form = SalaDeCineForm(instance=sala)
    return render(request, 'sala_de_cine_form.html', {'form': form})

def sala_de_cine_delete(request, pk):
    sala = SalaDeCine.objects.get(pk=pk)
    if request.method == 'POST':
        sala.delete()
        return redirect('sala_de_cine_list')
    return render(request, 'sala_de_cine_delete.html', {'sala': sala})


