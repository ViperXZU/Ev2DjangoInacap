from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Funcion, Peliculas, SalaDeCine
from .forms import FuncionForm, PeliculasForm, SalaDeCineForm

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
    
def funcion_list(request):
    # Obtener todas las funciones
    funciones = Funcion.objects.all().order_by('fecha_hora_inicio')
    
    # Filtros
    pelicula_id = request.GET.get('pelicula')
    sala_id = request.GET.get('sala')
    fecha = request.GET.get('fecha')
    
    if pelicula_id:
        funciones = funciones.filter(pelicula_id=pelicula_id)
    
    if sala_id:
        funciones = funciones.filter(sala_id=sala_id)
    
    if fecha:
        funciones = funciones.filter(fecha_hora_inicio__date=fecha)
    
    # Obtener todas las películas y salas para los filtros
    peliculas = Peliculas.objects.all()
    salas = SalaDeCine.objects.all()
    
    context = {
        'funciones': funciones,
        'peliculas': peliculas,
        'salas': salas
    }
    
    return render(request, 'funciones_list.html', context)

def funcion_create(request):
    error_message = None
    
    if request.method == 'POST':
        form = FuncionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Función creada exitosamente.')
                return redirect('funciones_list')
            except ValueError as e:
                error_message = str(e)
            except IntegrityError:
                error_message = "Ya existe una función en esta sala a la misma hora."
    else:
        form = FuncionForm()
    
    # Obtener todas las películas y salas para los selects
    peliculas = Peliculas.objects.all()
    salas = SalaDeCine.objects.all()
    
    context = {
        'form': form,
        'peliculas': peliculas,
        'salas': salas,
        'error_message': error_message
    }
    
    return render(request, 'funcionesForm.html', context)

def funcion_update(request, pk):
    funcion = get_object_or_404(Funcion, pk=pk)
    error_message = None
    
    if request.method == 'POST':
        form = FuncionForm(request.POST, instance=funcion)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Función actualizada exitosamente.')
                return redirect('funcion_list')
            except ValueError as e:
                error_message = str(e)
            except IntegrityError:
                error_message = "Ya existe una función en esta sala a la misma hora."
    else:
        form = FuncionForm(instance=funcion)
    
    # Obtener todas las películas y salas para los selects
    peliculas = Peliculas.objects.all()
    salas = SalaDeCine.objects.all()
    
    context = {
        'form': form,
        'peliculas': peliculas,
        'salas': salas,
        'error_message': error_message
    }
    
    return render(request, 'funcionesForm.html', context)

def funcion_delete(request, pk):
    funcion = get_object_or_404(Funcion, pk=pk)
    
    if request.method == 'POST':
        funcion.delete()
        messages.success(request, 'Función eliminada exitosamente.')
        return redirect('funcion_list')
    
    return redirect('funcion_list')
    


