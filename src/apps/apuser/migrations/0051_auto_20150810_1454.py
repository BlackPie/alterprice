# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0050_payment_bill_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='alterpriceuser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 10, 11, 54, 35, 535986, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='operator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='operator', verbose_name='Оператор', blank=True, default=None, null=True),
        ),
    ]
