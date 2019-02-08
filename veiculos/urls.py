from django.urls import path, include
from .views import veiculos_lista, veiculos_cadastro, veiculos_editar, veiculos_delete

urlpatterns =[
    path('', veiculos_lista, name = 'veiculos'),
    path('lista/', veiculos_lista, name = 'veiculos_lista'),
    path('cadastro/', veiculos_cadastro, name = 'cadastro' ),
    path('editar/<int:id>/', veiculos_editar, name = "veiculos_editar"),
    path('delete/<int:id>/', veiculos_delete, name="veiculos_delete")
]