# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-23 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('burial_form', '0005_auto_20170923_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formno1',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Статус обработки заявления'),
        ),
        migrations.AlterField(
            model_name='formno1',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_form', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
