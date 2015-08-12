# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20150731_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='loaded',
            field=models.BooleanField(default=True),
        ),
    ]
