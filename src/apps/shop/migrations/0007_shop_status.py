# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150610_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='status',
            field=models.PositiveSmallIntegerField(verbose_name='Статус', choices=[(0, 'Не активeн'), (1, 'Активен')], default=1),
        ),
    ]
