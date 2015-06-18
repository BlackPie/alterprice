# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productshop',
            name='price',
        ),
        migrations.RemoveField(
            model_name='productshopdelivery',
            name='price',
        ),
    ]
