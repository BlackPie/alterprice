# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_city'),
        ('shop', '0009_remove_shop_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(verbose_name='Город', to='catalog.City', blank=True, null=True, default=None),
        ),
    ]
