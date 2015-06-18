# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20150618_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='price',
            field=models.IntegerField(verbose_name='Цена', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productshopdelivery',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена доставки', blank=True, default=None),
        ),
    ]
