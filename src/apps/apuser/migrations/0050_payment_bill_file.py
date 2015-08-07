# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apuser.models.payment


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0049_auto_20150807_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bill_file',
            field=apuser.models.payment.LimitedFileField(upload_to='', blank=True),
        ),
    ]
