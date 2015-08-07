# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0048_auto_20150729_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alterpriceuser',
            options={'verbose_name_plural': 'Пользователи', 'ordering': ('email',), 'verbose_name': 'Пользователь'},
        ),
        migrations.AlterModelOptions(
            name='operatorprofile',
            options={'verbose_name_plural': 'Операторы', 'ordering': ('name',), 'verbose_name': 'Оператор'},
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Оплачен'), (0, 'Не оплачен')], verbose_name='Статус платежа', default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='operator',
            field=models.ForeignKey(null=True, verbose_name='Оператор', blank=True, default=None, to='apuser.OperatorProfile', related_name='operator'),
        ),
    ]
