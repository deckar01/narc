# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_project_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='path',
            field=models.CharField(blank=True, default='', max_length=2083),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(blank=True, default='', max_length=2083),
        ),
    ]
