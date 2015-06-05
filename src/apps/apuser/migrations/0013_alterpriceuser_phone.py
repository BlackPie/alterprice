# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0012_auto_20150605_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='alterpriceuser',
            name='phone',
            field=models.CharField(default=None, verbose_name='Телефон', blank=True, max_length=100, null=True),
        ),
    ]
