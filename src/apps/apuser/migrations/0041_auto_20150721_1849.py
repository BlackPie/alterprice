# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0040_auto_20150720_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='client',
            field=models.ForeignKey(default=1, verbose_name='Клиент', to='apuser.ClientProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='robokassa_success',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
    ]
