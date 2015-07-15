# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0038_auto_20150715_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='is_active',
            field=models.BooleanField(verbose_name='Активен', help_text='Неактивен если закончились деньги на балансе', default=False),
        ),
    ]
