# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20150630_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopyml',
            name='name',
            field=models.CharField(verbose_name='Название YML', default=1, max_length=255),
            preserve_default=False,
        ),
    ]
