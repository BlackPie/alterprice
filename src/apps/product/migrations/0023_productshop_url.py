# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_productshop_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshop',
            name='url',
            field=models.URLField(null=True, blank=True, verbose_name='Ссылка на товар', default=None),
        ),
    ]
