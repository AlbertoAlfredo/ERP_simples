from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculos
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


def veiculos_editar(request, id):
    veiculos = get_object_or_404(Veiculos, pk=id)
    form = VeiculosForm(request.POST or None, request.FILES or None, instance=veiculos)

    if form.is_valid():
        form.save()
        return redirect('veiculos_lista')
    return render(request, 'veiculos_editar.html', {'form':form})


def veiculos_delete(request, id):
    veiculos = get_object_or_404(Veiculos, pk=id)

    if request.method == "POST":
        veiculos.delete()
        return redirect('veiculos_lista')
    return render(request, 'veiculos_delete.html', {'veiculos':veiculos})
