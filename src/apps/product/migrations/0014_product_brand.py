# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('product', '0013_productshopdelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=None, null=True, verbose_name='Бренд', to='brand.Brand', blank=True),
        ),
    ]
