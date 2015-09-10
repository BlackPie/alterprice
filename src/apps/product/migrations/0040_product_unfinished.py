# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0039_auto_20150821_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unfinished',
            field=models.BooleanField(default=False, verbose_name='Нераспределённый товар'),
        ),
    ]
