# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0014_alterpriceuser_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alterpriceuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='alterpriceuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='alterpriceuser',
            name='phone',
        ),
    ]
