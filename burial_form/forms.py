# -*- coding: utf-8 -*-
from django import forms
from .models import FormNo1


class FormNo1Form(forms.ModelForm):
    class Meta:
        model = FormNo1
        exclude = ('status',)
