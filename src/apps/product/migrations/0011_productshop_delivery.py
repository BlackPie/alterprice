# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productshop_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='delivery',
            field=models.PositiveSmallIntegerField(choices=[(0, 'С доставкой'), (1, 'Самовывоз')], default=0, verbose_name='Тип доставки'),
        ),
    ]
