# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_property'),
        ('product', '0021_auto_20150623_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='currency',
            field=models.ForeignKey(verbose_name='Валюта', null=True, default=None, to='catalog.Currency', blank=True),
        ),
    ]
