# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20150618_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='city',
        ),
    ]
