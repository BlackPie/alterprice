# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_shop_ym_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Статус', choices=[(0, 'Не активeн'), (1, 'Активен')]),
        ),
    ]
