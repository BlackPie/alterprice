# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_shop_raiting'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 10, 11, 54, 43, 465136, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
