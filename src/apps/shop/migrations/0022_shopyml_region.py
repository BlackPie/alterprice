# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20150715_1342'),
        ('shop', '0021_remove_shopyml_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopyml',
            name='region',
            field=models.ForeignKey(default=1, to='catalog.City'),
            preserve_default=False,
        ),
    ]
