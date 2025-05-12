from django.shortcuts import render, redirect
from .forms import ClientForm, VehicleForm, ServiceForm
from .models import Client, Vehicle, Service

def client_list(request):
    clients = Client.objects.all()

    name_search = request.GET.get('name_search')
    email_search = request.GET.get('email_search')

    if name_search:
        clients = clients.filter(name__icontains=name_search)
    if email_search:
        clients = clients.filter(email__icontains=email_search)

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
    
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    brand_search = request.GET.get('brand_search')
    model_search = request.GET.get('model_search')
    year_search = request.GET.get('year_search')
    client_search = request.GET.get('client_search')

    if brand_search:
        vehicles = vehicles.filter(brand__icontains=brand_search)
    if model_search:
        vehicles = vehicles.filter(model__icontains=model_search)
    if year_search:
        vehicles = vehicles.filter(year__icontains=year_search) # Usar __exact si el año debe ser una coincidencia exacta
    if client_search:
        vehicles = vehicles.filter(client__name__icontains=client_search)

    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

def vehicle_update(request, plate):
    vehicle = Vehicle.objects.get(pk=plate)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_form.html', {'form': form})

def vehicle_delete(request, plate):
    vehicle = Vehicle.objects.get(pk=plate)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    
def service_list(request):
    services = Service.objects.all()
    plate_filter = request.GET.get('plate_search')
    date_filter = request.GET.get('date')

    if plate_filter:
        services = services.filter(vehicle__plate__icontains=plate_filter)
    if date_filter:
        services = services.filter(date__icontains=date_filter)

    return render(request, 'services_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_form.html', {'form': form})

def service_update(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_form.html', {'form': form})

def service_delete(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    
    