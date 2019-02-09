from django.urls import path, include
from .views import produtos_lista, produtos_cadastro, produtos_editar, produtos_delete

urlpatterns =[
    path('', produtos_lista, name = 'produtos'),
    path('lista/', produtos_lista, name = 'produtos_lista'),
    path('cadastro/', produtos_cadastro, name = 'produtos_cadastro' ),
    path('editar/<int:id>/', produtos_editar, name = "produtos_editar"),
    path('delete/<int:id>/', produtos_delete, name="produtos_delete")
]