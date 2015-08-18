# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_categorystatistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorystatistics',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
