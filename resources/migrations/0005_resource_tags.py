# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-12 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='resources', to='resources.Tag', verbose_name='Etiquetas'),
        ),
    ]