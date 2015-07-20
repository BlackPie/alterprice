# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0039_clientprofile_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicerequest',
            name='user',
        ),
        migrations.AddField(
            model_name='invoicerequest',
            name='client',
            field=models.ForeignKey(default=1, to='apuser.ClientProfile', verbose_name='Клиент'),
            preserve_default=False,
        ),
    ]
