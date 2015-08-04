# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20150729_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='raiting',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Рейтинг', blank=True),
        ),
    ]
