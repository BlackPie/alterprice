# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0030_auto_20150630_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alterpriceuser',
            name='status',
            field=models.PositiveSmallIntegerField(verbose_name='Статус', default=0, choices=[(0, 'Не активeн'), (1, 'Активен')]),
        ),
    ]
