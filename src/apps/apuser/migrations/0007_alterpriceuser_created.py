# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0006_alterpriceuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='alterpriceuser',
            name='created',
            field=models.DateTimeField(verbose_name='Дата регистрации', default=datetime.datetime(2015, 6, 4, 11, 43, 14, 207197), auto_now_add=True),
            preserve_default=False,
        ),
    ]
