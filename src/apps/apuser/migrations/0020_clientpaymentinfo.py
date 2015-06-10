# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0019_auto_20150609_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPaymentInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('org_name', models.CharField(verbose_name='Название организации', max_length=255)),
                ('inn', models.CharField(verbose_name='ИНН', max_length=255)),
                ('kpp', models.CharField(verbose_name='КПП', max_length=255)),
                ('bik', models.CharField(verbose_name='БИК', max_length=255)),
                ('rs', models.CharField(verbose_name='Р/С', max_length=255)),
                ('corp_bill', models.CharField(verbose_name='Кор. счет', max_length=255)),
                ('bank_name', models.CharField(verbose_name='Название банка', max_length=255)),
                ('contact_name', models.CharField(verbose_name='ФИО контактного лица', max_length=255)),
                ('contact_phone', models.CharField(verbose_name='Телефон контактного лица', max_length=255)),
                ('legal_address', models.CharField(verbose_name='Юридический адрес', max_length=255)),
                ('post_address', models.CharField(verbose_name='Почтовый адрес', max_length=255)),
                ('client', models.ForeignKey(verbose_name='Клиент', to='apuser.ClientProfile')),
            ],
            options={
                'verbose_name': 'Платежные данные клиента',
                'verbose_name_plural': 'Платежные данные клиентов',
            },
        ),
    ]
