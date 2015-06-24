# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandManager',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='ym_id',
            field=models.IntegerField(verbose_name='Yandex Market ID', default=1),
            preserve_default=False,
        ),
    ]
