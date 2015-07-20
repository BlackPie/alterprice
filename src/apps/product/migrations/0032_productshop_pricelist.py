# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20150720_1937'),
        ('product', '0031_remove_productshop_shopyml'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='pricelist',
            field=models.ForeignKey(blank=True, verbose_name='YML файл', to='shop.Pricelist', default=None, null=True),
        ),
    ]
