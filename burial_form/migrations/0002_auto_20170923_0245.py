# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-22 23:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burial_form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deathcertificate',
            old_name='dcaddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='deathcertificate',
            old_name='dcnumber',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='deathcertificate',
            old_name='dcperson',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='deathcertificate',
            old_name='dcseries',
            new_name='series',
        ),
    ]