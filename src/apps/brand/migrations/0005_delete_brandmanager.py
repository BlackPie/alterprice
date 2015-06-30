# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_brand_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BrandManager',
        ),
    ]
