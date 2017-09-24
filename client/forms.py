# -*- coding:utf-8 -*-
from django import forms
from .models import Region, \
                    Profile, \
                    District, \
                    Organization, \
                    AuthorizedPerson, \
                    AdminOfOrganization


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['full_name', 'inn', 'kpp', 'district', 'legal_address', 
                  'actual_address', 'no_phone', 'email', 'no_users']

