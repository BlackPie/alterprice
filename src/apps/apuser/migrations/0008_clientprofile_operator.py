# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0007_alterpriceuser_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='operator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None, null=True, related_name='operator', blank=True, verbose_name='Оператор'),
        ),
    ]
