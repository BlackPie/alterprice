# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0009_operatorprofile_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='approved',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Подтвержден'), (0, 'Не подтвержден')], verbose_name='Статус подтвержденности', default=0),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='date_approved',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата подтверждения', default=None),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='moderator',
            field=models.ForeignKey(related_name='moderator', verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
