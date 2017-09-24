# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import Region, \
                    Profile, \
                    District, \
                    Organization, \
                    AuthorizedPerson, \
                    AdminOfOrganization


class AuthorizedPersonInline(admin.TabularInline):
    model = AuthorizedPerson
    extra=1


class ContactPersonInline(admin.TabularInline):
    model = AdminOfOrganization
    extra=1


class OrganizationAdmin(admin.ModelAdmin):
    inlines = (AuthorizedPersonInline, ContactPersonInline)
    search_fields = ('inn', 
                     'kpp', 
                     'email', 
                     'no_phone', 
                     'full_name', 
                     'legal_address', 
                     'district__name', 
                     'actual_address')
    list_display = ('name', 'no_phone', 'created', 'no_users')


class DistrictInLine(admin.TabularInline):
    model = District
    search_fields = ('name', 'kind', 'okato', 'oktmo')


class RegionAdmin(admin.ModelAdmin):
    inlines = (DistrictInLine,)
    search_fields = ('name',)


class AuthorizedPersonAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(AuthorizedPerson, AuthorizedPersonAdmin)
admin.site.register(Profile, ProfileAdmin)
