# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0033_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancehistory',
            name='click',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Клик', to='apuser.Click', default=None),
        ),
    ]
