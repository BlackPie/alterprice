# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0045_remove_click_productshop'),
        ('catalog', '0013_auto_20150724_1609'),
        ('shop', '0024_pricelist_status'),
        ('product', '0034_auto_20150724_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url', models.URLField(verbose_name='Ссылка на товар', null=True, default=None, blank=True)),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('click_price', models.IntegerField(verbose_name='Цена клика', default=2)),
                ('currency', models.ForeignKey(to='catalog.Currency', default=None, verbose_name='Валюта', null=True, blank=True)),
                ('offercategory', models.ForeignKey(to='shop.OfferCategories', default=None, verbose_name='Категория предолжения', null=True, blank=True)),
                ('pricelist', models.ForeignKey(to='shop.Pricelist', default=None, verbose_name='YML файл', null=True, blank=True)),
                ('product', models.ForeignKey(verbose_name='Продукт', to='product.Product')),
                ('shop', models.ForeignKey(verbose_name='Магазин', to='shop.Shop')),
            ],
            options={
                'verbose_name': 'Магазин продукта',
                'verbose_name_plural': 'магазины продуктов',
            },
        ),
        migrations.CreateModel(
            name='OfferDelivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pickup', models.BooleanField(verbose_name='Самовывоз', default=True)),
                ('delivery', models.BooleanField(verbose_name='Доставка', default=True)),
                ('store', models.BooleanField(verbose_name='Наличие', default=True)),
                ('price', models.IntegerField(verbose_name='Цена доставки', null=True, default=None, blank=True)),
                ('productshop', models.OneToOneField(to='product.Offer', verbose_name='Магазин продукта')),
            ],
            options={
                'verbose_name': 'Доставка продукта',
                'verbose_name_plural': 'Доставка продуктов',
            },
        ),
        migrations.RemoveField(
            model_name='productshop',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='productshop',
            name='offercategory',
        ),
        migrations.RemoveField(
            model_name='productshop',
            name='pricelist',
        ),
        migrations.RemoveField(
            model_name='productshop',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productshop',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='productshopdelivery',
            name='productshop',
        ),
        migrations.DeleteModel(
            name='ProductShop',
        ),
        migrations.DeleteModel(
            name='ProductShopDelivery',
        ),
    ]
