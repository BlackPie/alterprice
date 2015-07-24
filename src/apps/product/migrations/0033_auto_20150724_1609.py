# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_productshop_pricelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ym_id',
            field=models.IntegerField(blank=True, verbose_name='Yandex Market ID', null=True),
        ),
    ]
