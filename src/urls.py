# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.static import serve

from client.views import registrate
from burial_form.views import new_form_No1



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'), 
    url(r'^рег', registrate, name='registrate'),
#    url(r'^accounts/', include('registration.backends.default.urls')), 
    url(r'^adm/', admin.site.urls), 
    url(r'^создать/форма_N1/$', new_form_No1, name='create_form1')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': '/home/alex/CodeInWork/knipo/static',
        }),
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
