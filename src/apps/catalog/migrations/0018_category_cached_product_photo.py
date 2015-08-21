# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_city_default_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cached_product_photo',
            field=models.CharField(verbose_name='Временное фото', default=None, null=True, max_length=255, blank=True),
        ),
    ]
