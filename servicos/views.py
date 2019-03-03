from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicos
from django.db.models import Q
from .forms import ServicosForm
from django.core.paginator import Paginator, InvalidPage


# Create your views here.
def servicos_lista(request):
    if request.GET:
        slug = request.GET['search_box']
        servicos = Servicos.objects.filter(Q(codigo__icontains=slug) | Q(nome__icontains=slug) | Q(preco__icontains=slug) | Q(etc__icontains=slug))
    else:
        servicos = Servicos.objects.all()
    servicos = Servicos.objects.all()
    paginator = Paginator(servicos, 10)
    page = request.GET.get('page')
    servicos = paginator.get_page(page)
    return render(request, 'servicos_lista.html', {'servicos': servicos})


def servicos_cadastro(request):
    form = ServicosForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('servicos')
    return render(request, 'servicos_cadastro.html', {"form":form})


def servicos_editar(request, id):
    servicos = get_object_or_404(Servicos, pk=id)
    form = ServicosForm(request.POST or None, request.FILES or None, instance=servicos)

    if form.is_valid():
        form.save()
        return redirect('servicos_lista')
    return render(request, 'servicos_editar.html', {'form':form})


def servicos_delete(request, id):
    servicos = get_object_or_404(Servicos, pk=id)

    if request.method == "POST":
        servicos.delete()
        return redirect('servicos_lista')
    return render(request, 'servicos_delete.html', {'servicos':servicos})
