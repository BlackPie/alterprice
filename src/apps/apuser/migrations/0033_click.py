# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_remove_productshop_point'),
        ('apuser', '0032_balancehistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user_ip', models.GenericIPAddressField(blank=True, default=None, verbose_name='IP пользователя', null=True)),
                ('productshop', models.ForeignKey(verbose_name='Магази продукта', to='product.ProductShop')),
            ],
            options={
                'verbose_name': 'Клик по товару',
                'verbose_name_plural': 'Клики по товару',
            },
        ),
    ]
