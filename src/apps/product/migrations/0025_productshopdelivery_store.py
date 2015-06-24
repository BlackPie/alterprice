# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_productshop_offercategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshopdelivery',
            name='store',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
    ]
