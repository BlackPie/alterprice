# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0003_remove_brand_ym_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='code',
            field=models.CharField(verbose_name='VendorCode', default=1, max_length=255, db_index=True),
            preserve_default=False,
        ),
    ]
