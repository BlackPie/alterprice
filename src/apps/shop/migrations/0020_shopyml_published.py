# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20150702_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopyml',
            name='published',
            field=models.BooleanField(verbose_name='Опублкован?', default=False),
        ),
    ]
