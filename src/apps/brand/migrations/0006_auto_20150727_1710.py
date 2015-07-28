# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0005_delete_brandmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='code',
            field=models.CharField(verbose_name='VendorCode', null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(verbose_name='Название', max_length=255, db_index=True),
        ),
    ]
