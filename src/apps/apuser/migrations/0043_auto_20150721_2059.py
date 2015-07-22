# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0042_invoicerequest_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.ForeignKey(null=True, verbose_name='Валюта', blank=True, to='catalog.Currency'),
        ),
    ]
