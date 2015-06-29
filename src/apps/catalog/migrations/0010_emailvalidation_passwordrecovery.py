# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalog.models.token
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0009_category_ym_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailValidation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sending_status', models.PositiveSmallIntegerField(verbose_name='Статус отправки', db_index=True, choices=[(0, 'В ожидании'), (1, 'Отправлено'), (2, 'Отменено')], default=0)),
                ('sending_date', models.DateTimeField(verbose_name='Дата отправки', null=True, blank=True, default=None)),
                ('email', models.EmailField(max_length=254, db_index=True, verbose_name='Проверяемый E-mail')),
                ('token', models.CharField(max_length=255, db_index=True, verbose_name='Токен активации', unique=True)),
                ('status', models.SmallIntegerField(verbose_name='Статус активации', db_index=True, choices=[(0, 'Не подтвержден'), (1, 'Подтвержден'), (2, 'Не релевантный')], default=0)),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('confirmed', models.DateTimeField(verbose_name='Дата подтверждения активации (UTC)', null=True, blank=True)),
                ('expiration_date', models.DateTimeField(verbose_name='Дата истечения', db_index=True, default=catalog.models.token.email_expiration_date)),
                ('user', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Активация электронной почты',
                'verbose_name_plural': 'Активации электронной почты',
            },
        ),
        migrations.CreateModel(
            name='PasswordRecovery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sending_status', models.PositiveSmallIntegerField(verbose_name='Статус отправки', db_index=True, choices=[(0, 'В ожидании'), (1, 'Отправлено'), (2, 'Отменено')], default=0)),
                ('sending_date', models.DateTimeField(verbose_name='Дата отправки', null=True, blank=True, default=None)),
                ('token', models.CharField(max_length=32, verbose_name='Токен подтверждения', unique=True)),
                ('status', models.PositiveSmallIntegerField(verbose_name='Статус', db_index=True, choices=[(0, 'Выслан'), (1, 'Восстановлен'), (2, 'Истек')], default=0)),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('expiration_date', models.DateTimeField(verbose_name='Дата истечения', db_index=True, default=catalog.models.token.recovery_expiration_date)),
                ('recovery_date', models.DateTimeField(verbose_name='Дата восстановления', null=True, blank=True, default=None)),
                ('user', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Токен восстановления пароля',
                'verbose_name_plural': 'Токены восстановления паролей',
            },
        ),
    ]
