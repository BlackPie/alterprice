# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0022_remove_clientprofile_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='moderator',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, default=None, verbose_name='Модератор'),
        ),
    ]
