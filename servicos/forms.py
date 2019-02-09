from django.forms import ModelForm
from .models import Servicos


class ServicosForm(ModelForm):
    class Meta:
        model = Servicos
        fields = ['codigo', 'nome', 'preco', 'etc']
