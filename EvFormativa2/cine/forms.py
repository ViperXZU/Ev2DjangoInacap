from django import forms
from .models import Peliculas, SalaDeCine, Funcion


class PeliculasForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SalaDeCineForm(forms.ModelForm):
    class Meta:
        model = SalaDeCine
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipoDeSala': forms.Select(attrs={'class': 'form-control'}),
        }

class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = 'pelicula', 'sala', 'fecha_hora_inicio'
        widgets = {
            'pelicula': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-control'}),
            'fecha_hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


