# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20150623_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='ym_id',
        ),
    ]
