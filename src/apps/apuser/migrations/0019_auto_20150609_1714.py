# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0018_auto_20150608_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='user',
            field=models.OneToOneField(related_name='admin_user', verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='moderator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Модератор'),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='user',
            field=models.OneToOneField(related_name='client_user', verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operatorprofile',
            name='user',
            field=models.OneToOneField(related_name='operator_user', verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
        ),
    ]
