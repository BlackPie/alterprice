# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0036_auto_20150713_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл счета')),
                ('company_name', models.CharField(max_length=255, verbose_name='Компания')),
                ('inn', models.CharField(max_length=255, verbose_name='ИНН')),
                ('kpp', models.CharField(max_length=255, verbose_name='КПП')),
                ('bik', models.CharField(max_length=255, verbose_name='БИК')),
                ('rs', models.CharField(max_length=255, verbose_name='Рассчетный счет')),
                ('ks', models.CharField(max_length=255, verbose_name='Корреспондетский счет')),
                ('bank_name', models.CharField(max_length=255, verbose_name='Название банка')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО контактного лица')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон контактного лица')),
                ('legal_address', models.CharField(max_length=255, verbose_name='Юридический адрес')),
                ('post_address', models.CharField(max_length=255, verbose_name='Почтовый адрес')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
            ],
        ),
    ]
