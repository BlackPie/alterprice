# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_shopyml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(blank=True, verbose_name='Адресс', max_length=255, null=True, default=None),
        ),
        migrations.AlterField(
            model_name='shopyml',
            name='yml_url',
            field=models.URLField(verbose_name='YMl url'),
        ),
    ]
