# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0027_clientprofile_ownership_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='company',
            field=models.CharField(default=None, null=True, max_length=255, verbose_name='Название компании', blank=True),
        ),
    ]
