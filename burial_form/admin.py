# -*- coding: UTF-8 -*-
from django.contrib import admin

from catalog.models import Cemetery
from .models import Work,    \
                    Place,    \
                    Burial,    \
                    DeadMen,    \
                    FormNo1,     \
                    BaseForm,     \
                    Structure,     \
                    Declarant,      \
                    IdDocument,      \
                    DeathCertificate, \
                    AdditionalDocument
from client.models import Region,       \
                          Person,        \
                          District,       \
                          Organization,    \
                          AuthorizedPerson, \
                          AdminOfOrganization 


class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('name', 'sector_number', 'row_number', 
                   'burial_number', 'burial_resp')
    save_on_top = True


class WorkAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    save_on_top = True


class StructureAdmin(admin.ModelAdmin):
    search_fields = ()
    save_on_top = True


class BurialAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(Place, PlaceAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(Burial, BurialAdmin)

                #   Region
                #   Profile
                #   District
                #   Organization
                #   AuthorizedPerson
                #   AdminOfOrganization


#class DeclarantInline(admin.TabularInline):
#    model = Declarant
#    extra=1
#
#
#class BurialInline(admin.TabularInline):
#    model = Burial
#    extra=1
#
#
#class CemeteryInline(admin.TabularInline):
#    model = Cemetery
#    extra=1
#
#
# class _Inline(admin.TabularInline):
#     model = _
#     extra=1
# 
# 
# class _Inline(admin.TabularInline):
#     model = _
#     extra=1
# 
# 
# class _Inline(admin.TabularInline):
#     model = _
#     extra=1


class FormNo1Admin(admin.ModelAdmin):
    pass
#    inlines = (DeclarantInline, BurialInline, CemeteryInline)
#    search_fields = ()
#    list_display = ()


admin.site.register(FormNo1, FormNo1Admin)
