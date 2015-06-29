# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0028_clientprofile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Город', null=True, default=None, blank=True),
        ),
    ]
