# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150610_1752'),
        ('product', '0002_productproperty'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductShop',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('product', models.ForeignKey(verbose_name='Продукт', to='product.Product')),
                ('shop', models.ForeignKey(verbose_name='Магазин', to='shop.Shop')),
            ],
            options={
                'verbose_name_plural': 'магазины продуктов',
                'verbose_name': 'Магазин продукта',
            },
        ),
    ]
