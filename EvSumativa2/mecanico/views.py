from django.shortcuts import render, redirect, request
from .forms import ClientForm, VehicleForm, ServiceForm
from .models import Client, Vehicle, Service

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    
