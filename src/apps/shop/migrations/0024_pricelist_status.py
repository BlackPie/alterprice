# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20150720_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelist',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, 'Новый'), (2, 'Обработан'), (3, 'Невозможно обработать')]),
        ),
    ]
