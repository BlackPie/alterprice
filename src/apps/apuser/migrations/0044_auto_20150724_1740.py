# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0043_auto_20150721_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoicerequest',
            options={'verbose_name_plural': 'Запросы счетов', 'verbose_name': 'Запрос счета'},
        ),
    ]
