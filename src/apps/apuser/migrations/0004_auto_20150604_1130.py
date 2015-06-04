# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0003_auto_20150604_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user', models.OneToOneField(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Профили операторов',
                'verbose_name': 'Профиль оператора',
            },
        ),
        migrations.AlterModelOptions(
            name='adminprofile',
            options={'verbose_name_plural': 'Профили администраторов', 'verbose_name': 'Профиль администратора'},
        ),
    ]
