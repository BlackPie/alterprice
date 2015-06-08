# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0016_auto_20150608_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorprofile',
            name='last_name',
            field=models.CharField(null=True, verbose_name='Фамилия', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='operatorprofile',
            name='name',
            field=models.CharField(null=True, verbose_name='Имя', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='operatorprofile',
            name='phone',
            field=models.CharField(default=None, null=True, verbose_name='Телефон', max_length=100, blank=True),
        ),
    ]
