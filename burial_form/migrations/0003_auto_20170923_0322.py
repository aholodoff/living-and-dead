# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-23 00:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('burial_form', '0002_auto_20170923_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('S', 'Одиночное'), ('R', 'Родственное'), ('F', 'Cемейное'), ('W', 'Воинское'), ('H', 'Почетное')], default='R', max_length=1, verbose_name='Вид захоронения')),
                ('option', models.CharField(choices=[('P', 'Настоящее'), ('F', 'Будующее')], default='P', max_length=1, verbose_name='Тип захоронения')),
                ('info', models.TextField(blank=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name_plural': 'Захоронения',
                'verbose_name': 'Захоронение',
            },
        ),
        migrations.CreateModel(
            name='DeadMen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('sur_name', models.CharField(blank=True, max_length=256, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('no_phone', models.TextField(blank=True, verbose_name='Контактный телефон')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время внесения в базу')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения в базе')),
                ('date_of_death', models.DateField(verbose_name='Дата смерти умершего')),
                ('relation', models.CharField(default='Мать', max_length=64, verbose_name='Степень родства по отношению к заявителю')),
                ('declarant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dead_men', to='burial_form.Declarant')),
            ],
            options={
                'verbose_name_plural': 'Покойные',
                'verbose_name': 'Покойный',
            },
        ),
        migrations.CreateModel(
            name='IdDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=64, verbose_name='Паспорт')),
                ('series', models.CharField(max_length=8, verbose_name='Серия')),
                ('number', models.CharField(max_length=16, verbose_name='Номер')),
                ('address', models.CharField(blank=True, max_length=512, verbose_name='Адрес регистрации по месту жительства')),
                ('issued_by', models.CharField(blank=True, max_length=512, verbose_name='Кем выдан')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burial_form.Declarant')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название участка')),
                ('sector_number', models.CharField(max_length=128, verbose_name='Номер сектора')),
                ('row_number', models.CharField(max_length=128, verbose_name='Номер ряда')),
                ('burial_number', models.CharField(max_length=128, verbose_name='Номер могилы')),
                ('burial_resp', models.CharField(max_length=512, verbose_name='ФИО ответственного за захоронение')),
                ('cemetery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='catalog.Cemetery')),
                ('dead_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='burial_form.DeadMen')),
            ],
            options={
                'verbose_name_plural': 'Участки',
                'verbose_name': 'Участок',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(default=1, verbose_name='Статус обработки заявления')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Вид сооружения')),
            ],
            options={
                'verbose_name_plural': 'Виды сооружений',
                'verbose_name': 'Вид сооружения',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Вид работы на участке захоронения')),
            ],
            options={
                'verbose_name_plural': 'Виды работ',
                'verbose_name': 'Вид работы',
            },
        ),
        migrations.AddField(
            model_name='formno1',
            name='death_certificate',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='burial_form.DeathCertificate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deathcertificate',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='burial_form.DeadMen'),
        ),
        migrations.AlterField(
            model_name='formno1',
            name='burial',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='burial_form.Burial'),
        ),
        migrations.AlterField(
            model_name='formno1',
            name='dead_men',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='burial_form.DeadMen'),
        ),
        migrations.AlterField(
            model_name='formno1',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='burial_form.Place'),
        ),
        migrations.AlterField(
            model_name='formno1',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='burial_form.Status'),
        ),
    ]
