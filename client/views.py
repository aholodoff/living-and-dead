# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Это наша форма, которую мы определим в forms.py
from .models import Organization
from .forms import RegistrationForm


def registrate(request):
    if request.POST:
        data_in_form = RegistrationForm(request.POST, request.user)
        if data_in_form.is_valid():
            organization = data_in_form.save()
            return HttpResponse('Форма верна!')
    else:
        data_in_form = RegistrationForm(request.user)
    return render(request, 'custom/registrate.html', {'form': data_in_form})
