# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20150818_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='default_city',
            field=models.BooleanField(default=False),
        ),
    ]
