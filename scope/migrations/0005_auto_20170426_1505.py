# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scope', '0004_auto_20170426_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ('date_time',)},
        ),
    ]
