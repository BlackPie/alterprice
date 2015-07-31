# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_auto_20150730_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='ym_id',
            field=models.IntegerField(verbose_name='Market ID', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='contra',
            field=models.CharField(verbose_name='Достоинства', max_length=10000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='pro',
            field=models.CharField(verbose_name='Недостатки', max_length=10000, blank=True, null=True),
        ),
    ]
