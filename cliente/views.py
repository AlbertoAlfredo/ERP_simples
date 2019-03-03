from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from django.db.models import Q
from .forms import PersonForm
from django.core.paginator import Paginator, InvalidPage


# Create your views here.
def cliente_lista(request):
    if request.GET:
        slug = request.GET['search_box']
        clientes = Person.objects.filter(Q(first_name__icontains=slug) | Q(last_name__icontains=slug) | Q(phone__icontains=slug) | Q(text__icontains=slug))
    else:
        clientes = Person.objects.all()
    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    return render(request, 'cliente_lista.html', {'clientes':clientes})


def cliente_cadastro(request):
    form = PersonForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('cliente_lista')
    return render(request, 'cliente_cadastro.html', {'form':form})


def cliente_editar(request, id):
    cliente = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('cliente_lista')
    return render(request, 'cliente_editar.html', {'form':form})


def cliente_delete(request, id):
    cliente = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'cliente_delete.html', {'cliente':cliente})
