# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0005_clientprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='alterpriceuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(verbose_name='Статус', default=0, choices=[(0, 'Клиент'), (1, 'Оператор'), (2, 'Администратор')]),
        ),
    ]
