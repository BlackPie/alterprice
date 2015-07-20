# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20150715_1342'),
        ('product', '0031_remove_productshop_shopyml'),
        ('shop', '0022_shopyml_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricelist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('publish_status', models.PositiveSmallIntegerField(verbose_name='Статус публикации', default=0, choices=[(0, 'Не публикуется'), (1, 'Публикуется')])),
                ('publish_date', models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации', default=None)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('yml_url', models.URLField(verbose_name='YMl url')),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('currency', models.ForeignKey(blank=True, verbose_name='Валюта', to='catalog.Currency', default=None, null=True)),
                ('region', models.ForeignKey(to='catalog.City')),
            ],
            options={
                'verbose_name_plural': 'Прайс листы магазинов',
                'verbose_name': 'Прайс лист магазина',
            },
        ),
        migrations.RemoveField(
            model_name='shopyml',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='shopyml',
            name='region',
        ),
        migrations.RemoveField(
            model_name='shopyml',
            name='shop',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='city',
            new_name='region',
        ),
        migrations.RemoveField(
            model_name='offercategories',
            name='shopyml',
        ),
        migrations.DeleteModel(
            name='ShopYML',
        ),
        migrations.AddField(
            model_name='pricelist',
            name='shop',
            field=models.ForeignKey(verbose_name='Магазин', to='shop.Shop'),
        ),
        migrations.AddField(
            model_name='offercategories',
            name='pricelist',
            field=models.ForeignKey(verbose_name='Прайс лист', to='shop.Pricelist', default=1),
            preserve_default=False,
        ),
    ]
