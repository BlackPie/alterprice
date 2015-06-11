# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('property_name', models.CharField(verbose_name='Название свойства', max_length=255)),
                ('property_value', models.CharField(verbose_name='Значение свойства', max_length=255)),
                ('product', models.ForeignKey(verbose_name='Продукт', to='product.Product')),
            ],
            options={
                'verbose_name': 'Свойство продукта',
                'verbose_name_plural': 'Свойства продуктов',
            },
        ),
    ]
