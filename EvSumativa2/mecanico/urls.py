from django.urls import path
from .views import (client_create, client_update, client_delete, client_list,
                     vehicle_create, vehicle_update, vehicle_delete, vehicle_list,
                     service_create, service_update, service_delete, service_list)

urlpatterns = [
    path('clients/', client_list, name='client_list'),
    path('clients/create/', client_create, name='client_create'),
    path('clients/update/<int:pk>/', client_update, name='client_update'),
    path('clients/delete/<int:pk>/', client_delete, name='client_delete'),
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('vehicles/create/', vehicle_create, name='vehicle_create'),
    path('vehicles/update/<str:plate>/', vehicle_update, name='vehicle_update'),
    path('vehicles/delete/<str:plate>/', vehicle_delete, name='vehicle_delete'),
    path('services/', service_list, name='service_list'),
    path('services/create/', service_create, name='service_create'),
    path('services/update/<int:pk>/', service_update, name='service_update'),
    path('services/delete/<int:pk>/', service_delete, name='service_delete'),
]