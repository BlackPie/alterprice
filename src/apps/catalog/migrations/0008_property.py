# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('codename', models.CharField(verbose_name='Кодовое имя', unique=True, max_length=255, db_index=True)),
                ('ru_name', models.CharField(verbose_name='Русское название', blank=True, max_length=255, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Свойство продуктов',
                'verbose_name_plural': 'Свойства продуктов',
            },
        ),
    ]
