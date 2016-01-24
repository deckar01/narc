# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160124_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('version', models.CharField(default='0.0.0', max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='page',
            name='project',
        ),
        migrations.RemoveField(
            model_name='project',
            name='target_platforms',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='targetplatform',
            name='browser',
        ),
        migrations.RemoveField(
            model_name='targetplatform',
            name='operating_system',
        ),
        migrations.AlterField(
            model_name='browser',
            name='version',
            field=models.CharField(default='0.0.0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='operatingsystem',
            name='version',
            field=models.CharField(default='0.0.0', max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='TargetPlatform',
        ),
    ]
