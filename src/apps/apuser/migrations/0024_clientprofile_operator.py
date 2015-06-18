# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0023_auto_20150618_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='operator',
            field=models.ForeignKey(related_name='operator', null=True, verbose_name='Оператор', to=settings.AUTH_USER_MODEL, blank=True, default=None),
        ),
    ]
