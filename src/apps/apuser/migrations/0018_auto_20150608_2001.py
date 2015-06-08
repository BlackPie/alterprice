# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0017_auto_20150608_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='last_name',
            field=models.CharField(max_length=150, blank=True, verbose_name='Фамилия', null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='name',
            field=models.CharField(max_length=150, blank=True, verbose_name='Имя', null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='phone',
            field=models.CharField(max_length=100, blank=True, verbose_name='Телефон', default=None, null=True),
        ),
    ]
