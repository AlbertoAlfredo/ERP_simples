# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from controle_estoque.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('controle_estoque.views',
url(r'^$', 'home', name='home'),
url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
url(r'^lista/$', Lista.as_view(), name='lista'),
url(r'^admin/', include(admin.site.urls)),
)
