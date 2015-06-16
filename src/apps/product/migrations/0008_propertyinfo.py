# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20150616_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('property_name', models.CharField(max_length=255, verbose_name='Название свойства')),
                ('property_value', models.CharField(max_length=255, verbose_name='Значение свойства')),
                ('productproperty', models.ForeignKey(to='product.ProductProperty', verbose_name='Свойство')),
            ],
            options={
                'verbose_name': 'Данные свойства',
                'verbose_name_plural': 'Данные свойств',
            },
        ),
    ]
