from django.forms import ModelForm
from .models import Veiculos


class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculos
        fields = ['placa', 'marca', 'modelo', 'preco', 'etc', 'proprietario', 'foto']
