# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0035_auto_20150701_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alterpriceuser',
            name='created',
        ),
        migrations.RemoveField(
            model_name='alterpriceuser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='date_approved',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='moderator',
        ),
        migrations.AddField(
            model_name='alterpriceuser',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='Email подтвержден'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='checked',
            field=models.BooleanField(help_text='Модератор проверил и одобрил', default=False, verbose_name='Проверено'),
        ),
    ]
