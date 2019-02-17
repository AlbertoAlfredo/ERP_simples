"""micro_erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index
from cliente import urls as cliente_url
from produtos import urls as produtos_url
from veiculos import urls as veiculos_url
from servicos import urls as servicos_url
from carrinho_compras import urls as carrinho_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cliente/', include(cliente_url)),
    path('produtos/', include(produtos_url)),
    path('veiculos/', include(veiculos_url)),
    path('servicos/', include(servicos_url)),
    path('carrinho/', include(carrinho_url))
]
