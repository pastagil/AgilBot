# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0019_auto_20171118_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='chat_id',
            field=models.IntegerField(default=0, verbose_name='chat ID'),
            preserve_default=False,
        ),
    ]
