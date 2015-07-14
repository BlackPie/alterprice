# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_shopyml_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopyml',
            name='published',
        ),
    ]
