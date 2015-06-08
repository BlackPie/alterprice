# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0015_auto_20150608_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminprofile',
            name='last_name',
            field=models.CharField(blank=True, null=True, verbose_name='Фамилия', max_length=150),
        ),
        migrations.AddField(
            model_name='adminprofile',
            name='name',
            field=models.CharField(blank=True, null=True, verbose_name='Имя', max_length=150),
        ),
        migrations.AddField(
            model_name='adminprofile',
            name='phone',
            field=models.CharField(blank=True, null=True, verbose_name='Телефон', default=None, max_length=100),
        ),
    ]
