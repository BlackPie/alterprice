# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_city_slug'),
        ('product', '0016_auto_20150618_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, verbose_name='Категория', default=None, null=True, to='catalog.Category'),
        ),
    ]
