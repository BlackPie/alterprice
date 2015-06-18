# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0021_auto_20150610_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='operator',
        ),
    ]
