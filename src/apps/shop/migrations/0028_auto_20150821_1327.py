# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_shop_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offercategories',
            name='price',
            field=models.IntegerField(verbose_name='Цена за клик', default=3, null=True, blank=True),
        ),
    ]
