# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0037_invoicerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='user',
        ),
        migrations.AddField(
            model_name='balance',
            name='client',
            field=models.OneToOneField(verbose_name='Клиент', default=1, to='apuser.ClientProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='user',
            field=models.OneToOneField(verbose_name='Пользователь', related_name='client_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
