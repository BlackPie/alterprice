# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0002_adminprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='user',
            field=models.OneToOneField(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
        ),
    ]
