# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_productshop_shopyml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='shopyml',
            field=models.ForeignKey(to='shop.ShopYML', verbose_name='YML файл'),
        ),
    ]
