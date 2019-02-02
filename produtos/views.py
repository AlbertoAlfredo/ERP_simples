from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculos, Produtos, Servico
from .forms import VeiculosForm
from django.core.paginator import Paginator, InvalidPage


# Create your views here.
def veiculos_lista(request):
    veiculos = Veiculos.objects.all()
    paginator = Paginator(veiculos, 10)
    page = request.GET.get('page')
    veiculos = paginator.get_page(page)
    return render(request, 'veiculos_lista.html', {'veiculos': veiculos})


def veiculos_cadastro(request):
    form = VeiculosForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('veiculos')
    return render(request, 'veiculos_cadastro.html', {"form":form})
