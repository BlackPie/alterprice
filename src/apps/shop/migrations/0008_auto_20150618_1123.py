# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shop_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='moderator',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Модератор'),
        ),
    ]
