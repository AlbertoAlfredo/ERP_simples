from django.urls import path, include
from .views import produtos

urlpatterns =[
    path('', produtos, name = 'produtos')
]