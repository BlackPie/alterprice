# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0041_auto_20150721_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicerequest',
            name='created',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 21, 15, 5, 17, 861023, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
