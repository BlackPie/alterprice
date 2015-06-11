# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productshop',
            name='name',
        ),
        migrations.AddField(
            model_name='productshop',
            name='price',
            field=models.CharField(default=1, verbose_name='Цена', max_length=255),
            preserve_default=False,
        ),
    ]
