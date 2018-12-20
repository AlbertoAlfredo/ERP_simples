# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from controle_estoque.models import AdicionaProduto
from controle_estoque.forms import AdicionaProdutoForm

def home(request):
        return render(request,'index.html')

class Criar(CreateView):
        template_name = 'cadastro.html'
        model = AdicionaProduto
        success_url = reverse_lazy('lista')

class Lista(ListView):
        template_name = 'lista.html'
        model = AdicionaProduto
        context_object = 'nome'