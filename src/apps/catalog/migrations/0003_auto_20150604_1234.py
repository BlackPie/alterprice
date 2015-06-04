# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='click_count',
            field=models.IntegerField(verbose_name='Количество кликов', default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='goods_count',
            field=models.IntegerField(verbose_name='Количество товаров', default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(related_name='children', null=True, to='catalog.Category', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='shop_count',
            field=models.IntegerField(verbose_name='Количество магазинов', default=0),
        ),
    ]
