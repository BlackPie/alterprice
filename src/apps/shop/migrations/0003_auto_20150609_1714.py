# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_auto_20150609_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='approved',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Подтвержден'), (0, 'Не подтвержден')], verbose_name='Статус подтвержденности', default=0),
        ),
        migrations.AddField(
            model_name='shop',
            name='date_approved',
            field=models.DateTimeField(verbose_name='Дата подтверждения', default=None, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='moderator',
            field=models.ForeignKey(verbose_name='Модератор', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, related_name='owner'),
        ),
    ]
