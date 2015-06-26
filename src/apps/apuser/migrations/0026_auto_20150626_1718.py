# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0025_balance_bill_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Банковский счет'), (1, 'Онлайн оплата')], default=0, verbose_name='Тип оплаты'),
        ),
    ]
