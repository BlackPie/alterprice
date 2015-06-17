# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import catalog.models.category


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20150604_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='depth',
            field=models.IntegerField(verbose_name='Глубина наследования', default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerField(blank=True, verbose_name='Фото', null=True, upload_to=catalog.models.category.get_photo_path, default=None),
        ),
    ]
