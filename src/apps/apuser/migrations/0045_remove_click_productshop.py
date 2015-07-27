# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0044_auto_20150724_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='click',
            name='productshop',
        ),
    ]
