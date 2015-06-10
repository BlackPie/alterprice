# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20150610_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopYML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('yml_url', models.URLField(verbose_name='EMl')),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('shop', models.ForeignKey(verbose_name='Магазин', to='shop.Shop')),
            ],
            options={
                'verbose_name': 'YML файл магазина',
                'verbose_name_plural': 'YML файлы магазинов',
            },
        ),
    ]
