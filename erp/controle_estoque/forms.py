# -*- coding: utf-8 -*-
from django import forms
from models import AdicionaProduto

class InscricaoForm(forms.ModelForm):

        class Meta:
                model = AdicionaProduto