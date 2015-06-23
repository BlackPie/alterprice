# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_ym_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyinfo',
            name='productproperty',
        ),
        migrations.DeleteModel(
            name='PropertyInfo',
        ),
    ]
