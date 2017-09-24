# -*- coding: UTF-8 -*-
from django.contrib import admin
from client.models import Organization, AdminOfOrganization, AuthorizedPerson, \
                          District, Region, Person
from .models import Cemetery


class CemeteryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'info')
    search_fields = ('name', 'address', 'info')
    ordering = ('name', 'address')
    save_on_top = True


admin.site.register(Cemetery, CemeteryAdmin)
