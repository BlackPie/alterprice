# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Бренды',
                'verbose_name': 'Бренд',
            },
        ),
    ]
