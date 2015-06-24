# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_productshopdelivery_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productshop',
            name='point',
        ),
    ]
