# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0045_remove_click_productshop'),
        ('product', '0035_auto_20150727_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='offer',
            field=models.ForeignKey(to='product.Offer', verbose_name='Предложение', null=True, blank=True),
        ),
    ]
