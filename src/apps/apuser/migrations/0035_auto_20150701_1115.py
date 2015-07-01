# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0034_balancehistory_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_detail',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Основание платежа', choices=[(0, 'Платеж'), (1, 'Возврат средств')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Тип платежа', choices=[(0, 'Банковский счет'), (1, 'Онлайн оплата')]),
        ),
    ]
