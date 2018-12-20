# -*- coding: utf-8 -*-
from django.db import models


class AdicionaProduto(models.Model):
    cod_barras = models.IntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=288)
    valor = models.DecimalField(max_digits=22, decimal_places=2)

    class Meta:
        ordering = ['cod_barras']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def __unicode__(self):
        return self.nome
