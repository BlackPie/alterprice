# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0013_alterpriceuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='alterpriceuser',
            name='last_name',
            field=models.CharField(null=True, verbose_name='Фамилия', max_length=150, blank=True),
        ),
    ]
