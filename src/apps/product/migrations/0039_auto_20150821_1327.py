# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0038_product_loaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='click_price',
            field=models.IntegerField(verbose_name='Цена клика', default=3),
        ),
    ]
