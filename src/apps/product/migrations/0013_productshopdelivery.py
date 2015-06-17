# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_productshop_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductShopDelivery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pickup', models.BooleanField(verbose_name='Самовывоз', default=True)),
                ('delivery', models.BooleanField(verbose_name='Доставка', default=True)),
                ('price', models.CharField(blank=True, null=True, max_length=255, default=None, verbose_name='Цена доставки')),
                ('productshop', models.OneToOneField(verbose_name='Магазин продукта', to='product.ProductShop')),
            ],
            options={
                'verbose_name': 'Доставка продукта',
                'verbose_name_plural': 'Доставка продуктов',
            },
        ),
    ]
