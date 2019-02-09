from django.db import models

# Create your models here.


class Servicos(models.Model):
    codigo = models.CharField(max_length = 30, unique = True)
    nome = models.CharField(max_length = 50)
    preco = models.DecimalField(decimal_places=2, max_digits=9)
    etc = models.CharField(max_length = 144, null=True, blank=True)

    def __str__(self):
        return self.nome


