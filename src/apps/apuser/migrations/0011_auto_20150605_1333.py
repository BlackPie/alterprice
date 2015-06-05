# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0010_auto_20150605_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='moderator',
            field=models.ForeignKey(related_name='moderator', verbose_name='Модератор', to=settings.AUTH_USER_MODEL),
        ),
    ]
