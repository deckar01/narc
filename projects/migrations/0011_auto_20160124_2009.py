# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160124_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='page',
            name='path',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]
