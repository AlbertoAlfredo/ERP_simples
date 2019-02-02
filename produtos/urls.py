from django.urls import path, include
from .views import veiculos_lista, veiculos_cadastro

urlpatterns =[
    path('', veiculos_lista, name = 'veiculos'),
    path('cadastro/', veiculos_cadastro, name = 'cadastro' )
]