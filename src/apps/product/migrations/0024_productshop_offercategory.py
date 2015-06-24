# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_shopyml_currency'),
        ('product', '0023_productshop_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='offercategory',
            field=models.ForeignKey(verbose_name='Категория предолжения', blank=True, null=True, to='shop.OfferCategories', default=None),
        ),
    ]
