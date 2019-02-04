from django.db import models
from cliente.models import Person

# Create your models here.


class Veiculos(models.Model):
    placa = models.CharField(max_length = 8, unique = True)
    marca = models.CharField(max_length = 50)
    modelo = models.CharField(max_length = 50)
    preco = models.DecimalField(decimal_places=2, max_digits=9)
    etc = models.CharField(max_length = 144, null=True, blank=True)
    foto = models.ImageField(upload_to='veiculos_photos', null=True, blank=True)
    proprietario = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.marca + ' ' + self.modelo



#-Veiculo
#|_id
#|_proprietario
#|_marca / modelo
#|_placa
#-Servico
#|_preco
#|_descricao
#-Estoque
#|_fk-produto
#|_quantidade
#|_codigo