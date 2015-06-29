# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuser', '0026_auto_20150626_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='ownership_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Юридическое лицо'), (1, 'Физическое лицо')], verbose_name='Форма собственности', default=0),
        ),
    ]
