from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculos, Estoque
from django.core.paginator import Paginator, InvalidPage


# Create your views here.
def produtos(request):
    produtos = Veiculos.objects.all()
    paginator = Paginator(produtos, 10)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    return render(request, 'produtos_lista.html', {'produtos':produtos})

