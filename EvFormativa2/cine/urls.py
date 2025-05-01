from django.urls import path

from .views import (
    peliculas_list,
    peliculas_create,
    peliculas_update,
    peliculas_delete,
    sala_de_cine_list,
    sala_de_cine_create,
    sala_de_cine_update,
    sala_de_cine_delete,
)

urlpatterns = [
    path('peliculas/', peliculas_list, name='peliculas_list'),
    path('peliculas/create/', peliculas_create, name='peliculas_create'),
    path('peliculas/update/<int:pk>/', peliculas_update, name='peliculas_update'),
    path('peliculas/delete/<int:pk>/', peliculas_delete, name='peliculas_delete'),
    path('sala_de_cine/', sala_de_cine_list, name='sala_de_cine_list'),
    path('sala_de_cine/create/', sala_de_cine_create, name='sala_de_cine_create'),
    path('sala_de_cine/update/<int:pk>/', sala_de_cine_update, name='sala_de_cine_update'),
    path('sala_de_cine/delete/<int:pk>/', sala_de_cine_delete, name='sala_de_cine_delete'),
]
    


