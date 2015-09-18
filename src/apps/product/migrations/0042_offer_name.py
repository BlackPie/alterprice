# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0041_auto_20150917_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='name',
            field=models.CharField(null=True, max_length=255, blank=True, verbose_name='Название'),
        ),
    ]
