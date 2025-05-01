from django import forms
from .models import Peliculas
from .models import SalaDeCine

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


