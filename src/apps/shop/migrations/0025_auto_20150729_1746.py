# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_pricelist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='created',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='status',
        ),
    ]
