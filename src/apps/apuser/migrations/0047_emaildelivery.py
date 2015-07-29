# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0046_click_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailDelivery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('template', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=1000)),
                ('status', models.IntegerField(choices=[(0, 'Новое'), (1, 'Отправлено')], default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('context', django_extensions.db.fields.json.JSONField()),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
    ]
