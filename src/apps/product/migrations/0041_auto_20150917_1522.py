# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_product_unfinished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(verbose_name='Продукт', null=True, to='product.Product', blank=True),
        ),
    ]
