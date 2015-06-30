# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0029_clientprofile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='alterpriceuser',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(0, 'Не активeн'), (1, 'Активен')], verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='alterpriceuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
