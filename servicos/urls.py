from django.urls import path, include
from .views import servicos_lista, servicos_cadastro, servicos_editar, servicos_delete

urlpatterns =[
    path('', servicos_lista, name = 'servicos'),
    path('lista/', servicos_lista, name = 'servicos_lista'),
    path('cadastro/', servicos_cadastro, name = 'servicos_cadastro' ),
    path('editar/<int:id>/', servicos_editar, name = "servicos_editar"),
    path('delete/<int:id>/', servicos_delete, name="servicos_delete")
]