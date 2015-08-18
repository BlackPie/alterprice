# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20150818_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorystatistics',
            name='level',
        ),
        migrations.RemoveField(
            model_name='categorystatistics',
            name='name',
        ),
        migrations.AlterField(
            model_name='categorystatistics',
            name='created',
            field=models.DateField(),
        ),
    ]
