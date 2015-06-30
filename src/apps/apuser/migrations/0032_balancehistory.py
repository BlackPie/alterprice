# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0031_auto_20150630_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('previous_state', models.IntegerField(verbose_name='Предидущее состояние баланса', default=0)),
                ('change_value', models.IntegerField(verbose_name='Величина изменения', default=0)),
                ('new_state', models.IntegerField(verbose_name='Новое состояние', default=0)),
                ('reason', models.PositiveSmallIntegerField(choices=[(0, 'Клик'), (1, 'Пополнение'), (2, 'Восстановление')], verbose_name='Основание', default=0)),
                ('balance', models.ForeignKey(to='apuser.Balance', verbose_name='Баланс')),
                ('payment', models.ForeignKey(verbose_name='Платеж', to='apuser.Payment', null=True, blank=True, default=None)),
            ],
            options={
                'verbose_name_plural': 'Изменения баланса',
                'verbose_name': 'Изменение баланса',
            },
        ),
    ]
