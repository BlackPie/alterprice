# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_category_full_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='ym_id',
            field=models.IntegerField(blank=True, verbose_name='Yandex Market ID', null=True),
        ),
    ]
