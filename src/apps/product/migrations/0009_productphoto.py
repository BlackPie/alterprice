# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_propertyinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('photo', easy_thumbnails.fields.ThumbnailerField(default=None, verbose_name='Фото', blank=True, upload_to=product.models.get_photo_path, null=True)),
                ('product', models.ForeignKey(verbose_name='Продукт', to='product.Product')),
            ],
            options={
                'verbose_name': 'Фото продукта',
                'verbose_name_plural': 'Фото продуктов',
            },
        ),
    ]
