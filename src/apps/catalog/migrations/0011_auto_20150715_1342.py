# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_emailvalidation_passwordrecovery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='name', editable=False, unique=True),
        ),
    ]
