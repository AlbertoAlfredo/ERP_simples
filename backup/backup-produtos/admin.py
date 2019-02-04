from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Veiculos, Produtos, Servico

# Register your models here.
admin.site.register(Veiculos)
admin.site.register(Servico)
