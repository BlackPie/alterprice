# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150702_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='date_approved',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='moderator',
        ),
    ]
