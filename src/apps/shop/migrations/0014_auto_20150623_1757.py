# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_shopyml_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offercategories',
            name='price',
            field=models.IntegerField(verbose_name='Цена за клик', blank=True, null=True, default=2),
        ),
    ]
