# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_auto_20150702_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productshop',
            name='shopyml',
        ),
    ]
