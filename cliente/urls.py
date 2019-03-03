from django.urls import path
from .views import cliente_cadastro, cliente_lista, cliente_editar, cliente_delete

urlpatterns = [
    path('cadastro/', cliente_cadastro, name="cliente_cadastro"),
    path('', cliente_lista, name="cliente"),
    path('lista/', cliente_lista, name="cliente_lista"),
    path('editar/<int:id>/', cliente_editar, name="cliente_editar"),
    path('delete/<int:id>/', cliente_delete, name='cliente_delete'),
]
