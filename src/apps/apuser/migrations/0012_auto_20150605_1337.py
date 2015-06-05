# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0011_auto_20150605_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminprofile',
            options={'verbose_name_plural': 'Администраторы', 'verbose_name': 'Администратор'},
        ),
        migrations.AlterModelOptions(
            name='clientprofile',
            options={'verbose_name_plural': 'Клиенты', 'verbose_name': 'Клиент'},
        ),
        migrations.AlterModelOptions(
            name='operatorprofile',
            options={'verbose_name_plural': 'Операторы', 'verbose_name': 'Оператор'},
        ),
    ]
