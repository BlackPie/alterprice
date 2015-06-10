# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0020_clientpaymentinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpaymentinfo',
            name='client',
            field=models.OneToOneField(verbose_name='Клиент', to='apuser.ClientProfile'),
        ),
    ]
