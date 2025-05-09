from django import forms
from django.forms import ModelForm
from .models import Client, Vehicle, Service   

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'year', 'client']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['descripction', 'cost', 'vehicle', 'date']
        widgets = {
            'descripction': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

