# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_auto_20150624_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='ym_id',
        ),
    ]
