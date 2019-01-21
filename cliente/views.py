from django.shortcuts import render



# Create your views here.
def cliente_cadastro(request):
    return render(request, 'cliente_cadastro.html')