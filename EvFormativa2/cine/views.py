from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Peliculas, SalaDeCine
from .forms import PeliculasForm, SalaDeCineForm

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
    


