# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0015_auto_20171117_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='generic_url',
        ),
    ]