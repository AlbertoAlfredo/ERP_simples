from django.forms import ModelForm
from .models import Produtos


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['cod_barra', 'nome', 'preco', 'etc', 'foto']
