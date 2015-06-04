# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0008_clientprofile_operator'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorprofile',
            name='code',
            field=models.CharField(default=utils.helpers.generate_code, verbose_name='Код', max_length=5),
        ),
    ]
