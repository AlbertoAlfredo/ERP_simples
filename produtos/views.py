from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import ProdutosForm
from django.core.paginator import Paginator, InvalidPage


# Create your views here.
def produtos_lista(request):
    produtos = Produtos.objects.all()
    paginator = Paginator(produtos, 10)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    return render(request, 'produtos_lista.html', {'produtos': produtos})


def produtos_cadastro(request):
    form = ProdutosForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('produtos')
    return render(request, 'produtos_cadastro.html', {"form":form})


def produtos_editar(request, id):
    produtos = get_object_or_404(Produtos, pk=id)
    form = ProdutosForm(request.POST or None, request.FILES or None, instance=produtos)

    if form.is_valid():
        form.save()
        return redirect('produtos_lista')
    return render(request, 'produtos_editar.html', {'form':form})


def produtos_delete(request, id):
    produtos = get_object_or_404(Produtos, pk=id)

    if request.method == "POST":
        produtos.delete()
        return redirect('produtos_lista')
    return render(request, 'produtos_delete.html', {'produtos':produtos})
