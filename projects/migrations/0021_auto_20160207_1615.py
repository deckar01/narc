# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20160204_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='screen_height',
        ),
        migrations.RemoveField(
            model_name='device',
            name='screen_width',
        ),
        migrations.RemoveField(
            model_name='device',
            name='version',
        ),
    ]