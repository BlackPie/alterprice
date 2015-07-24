# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_auto_20150724_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('comment', models.CharField(max_length=10000, null=True, verbose_name='Комментарий', blank=True)),
                ('contra', models.CharField(max_length=10000, null=True, verbose_name='Недостатки', blank=True)),
                ('pro', models.CharField(max_length=10000, null=True, verbose_name='Достоинства', blank=True)),
                ('author', models.CharField(max_length=100, null=True, verbose_name='Имя автора', blank=True)),
                ('grade', models.IntegerField(verbose_name='Оценка')),
                ('agree', models.IntegerField(verbose_name='Согласно')),
                ('reject', models.IntegerField(verbose_name='Не согласно')),
                ('date', models.DateTimeField(verbose_name='Дата создания')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='details',
            field=django_extensions.db.fields.json.JSONField(null=True, verbose_name='Характеристики', blank=True),
        ),
        migrations.AddField(
            model_name='opinion',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
    ]
