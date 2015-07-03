# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_auto_20150702_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='click_price',
            field=models.IntegerField(default=2, verbose_name='Цена клика'),
        ),
        migrations.AlterField(
            model_name='productshop',
            name='shopyml',
            field=models.ForeignKey(blank=True, default=None, to='shop.ShopYML', null=True, verbose_name='YML файл'),
        ),
    ]
