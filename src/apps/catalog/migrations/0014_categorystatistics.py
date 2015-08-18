# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20150724_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStatistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.PositiveIntegerField(verbose_name='Уровень вложенности')),
                ('click_count', models.PositiveIntegerField(verbose_name='Количество кликов')),
                ('shop_count', models.PositiveIntegerField(verbose_name='Количество магазинов')),
                ('product_count', models.PositiveIntegerField(verbose_name='Количество товаров')),
                ('category', models.ForeignKey(to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Статистика категории',
                'verbose_name_plural': 'Статистика Категории',
            },
        ),
    ]
