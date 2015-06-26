# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_category_ym_id'),
        ('apuser', '0024_clientprofile_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('value', models.IntegerField(verbose_name='Значние', default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Баланс',
                'verbose_name_plural': 'Баланс',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('amount', models.IntegerField(verbose_name='Сумма', default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('payment_type', models.PositiveSmallIntegerField(verbose_name='Тип оплаты', default=0, choices=[(0, 'Банковыский счет'), (1, 'Онлайн оплата')])),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('amount', models.IntegerField(verbose_name='Сумма', default=0)),
                ('currency', models.ForeignKey(to='catalog.Currency', verbose_name='Валюта')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
    ]
