# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productproperty',
            name='property_name',
        ),
        migrations.RemoveField(
            model_name='productproperty',
            name='property_value',
        ),
        migrations.AddField(
            model_name='productproperty',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название', default='1'),
            preserve_default=False,
        ),
    ]
