# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_shopyml_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopyml',
            name='publish_date',
            field=models.DateTimeField(verbose_name='Дата публикации', null=True, default=None, blank=True),
        ),
        migrations.AddField(
            model_name='shopyml',
            name='publish_status',
            field=models.PositiveSmallIntegerField(verbose_name='Статус публикации', default=0, choices=[(0, 'Не публикуется'), (1, 'Публикуется')]),
        ),
    ]
