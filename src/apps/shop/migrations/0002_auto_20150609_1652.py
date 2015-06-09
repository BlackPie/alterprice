# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default=None, max_length=255, blank=True, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='shop',
            name='city',
            field=models.CharField(default=None, max_length=255, blank=True, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='shop',
            name='name',
            field=models.CharField(default='name_', max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='phone',
            field=models.CharField(default=None, max_length=255, blank=True, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='shop',
            name='site',
            field=models.URLField(default=None, blank=True, null=True, verbose_name='Сайт'),
        ),
    ]
