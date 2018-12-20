# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdicionaProduto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cod_barras', models.IntegerField(max_length=22)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=288)),
                ('valor', models.DecimalField(max_digits=22, decimal_places=2)),
            ],
            options={
                'verbose_name': 'nome',
                'verbose_name_plural': 'nomes',
                'ordering': ['cod_barras'],
            },
        ),
    ]
