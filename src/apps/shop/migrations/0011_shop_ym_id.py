# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_shop_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='ym_id',
            field=models.IntegerField(verbose_name='Yandex Market ID', default=1),
            preserve_default=False,
        ),
    ]
