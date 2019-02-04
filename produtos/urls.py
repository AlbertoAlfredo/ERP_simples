from django.urls import path, include
from .views import produtos_lista


urlpatterns=[
    path('', produtos_lista, name='produtos'),
]