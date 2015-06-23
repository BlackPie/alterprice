# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_city_slug'),
        ('shop', '0011_shop_ym_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.IntegerField(verbose_name='Цена за клик', default=None, blank=True, null=True)),
                ('category', models.ForeignKey(verbose_name='Категория', to='catalog.Category')),
                ('shopyml', models.ForeignKey(verbose_name='Предложение', to='shop.ShopYML')),
            ],
            options={
                'verbose_name': 'Категории предложения',
                'verbose_name_plural': 'Категории предложений',
            },
        ),
    ]
