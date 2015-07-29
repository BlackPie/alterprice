# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0047_emaildelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='limit_balance_email_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='zero_balance_email_send',
            field=models.BooleanField(default=False),
        ),
    ]
