# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
