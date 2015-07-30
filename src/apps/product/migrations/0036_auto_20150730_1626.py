# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0035_auto_20150727_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerdelivery',
            name='productshop',
        ),
        migrations.AlterModelOptions(
            name='opinion',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='offer',
            name='delivery_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='offer',
            name='pickup',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='OfferDelivery',
        ),
    ]
