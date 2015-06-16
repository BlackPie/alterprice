# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_productphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='point',
            field=models.IntegerField(verbose_name='Рейтинг', default=2),
        ),
    ]
