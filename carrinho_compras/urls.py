from django.urls import path
from .views import carrinho

urlpatterns = [
    path('', carrinho, name="carrinho")
]