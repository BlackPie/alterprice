# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150702_1511'),
        ('product', '0027_auto_20150702_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='shopyml',
            field=models.ForeignKey(to='shop.ShopYML', null=True, default=None, verbose_name='YML файл', blank=True),
        ),
    ]
