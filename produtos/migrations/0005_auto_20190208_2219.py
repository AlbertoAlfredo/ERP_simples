# Generated by Django 2.1.5 on 2019-02-09 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20190208_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='cod_barra',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
