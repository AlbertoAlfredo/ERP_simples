from django.urls import path
from .views import cliente_cadastro

urlpatterns = [
    path('cadastro/', cliente_cadastro),
]
