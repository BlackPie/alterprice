# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_property'),
        ('shop', '0012_offercategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopyml',
            name='currency',
            field=models.ForeignKey(blank=True, default=None, to='catalog.Currency', null=True, verbose_name='Валюта'),
        ),
    ]
