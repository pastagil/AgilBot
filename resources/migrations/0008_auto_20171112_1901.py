# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-12 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_resource_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='resources.Type', verbose_name='Tipo'),
        ),
    ]