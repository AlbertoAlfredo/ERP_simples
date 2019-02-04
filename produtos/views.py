from django.shortcuts import render


# Create your views here.
def produtos_lista(request):
    return render(request, 'produtos.html')
