# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150609_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', default=datetime.datetime(2015, 6, 10, 10, 41, 15, 242835)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='entity',
            field=models.CharField(verbose_name='Название юридического лица', max_length=255, default='entity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='ogrn',
            field=models.CharField(verbose_name='ОГРН', max_length=255, default='ogrn'),
            preserve_default=False,
        ),
    ]
