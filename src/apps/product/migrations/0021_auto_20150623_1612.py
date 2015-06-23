# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_property'),
        ('product', '0020_remove_productproperty_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productproperty',
            name='prop',
            field=models.ForeignKey(to='catalog.Property', verbose_name='Свойство', default=None, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productproperty',
            name='value',
            field=models.CharField(default=1, verbose_name='Значение свойства', max_length=255),
            preserve_default=False,
        ),
    ]
