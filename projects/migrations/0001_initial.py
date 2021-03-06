# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 18:18
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import private_media.storages
import projects.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('path', models.CharField(blank=True, default='', max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('browser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Browser')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Device')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.OperatingSystem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('private', models.BooleanField(default=True)),
                ('url', models.CharField(blank=True, default='', max_length=2083)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(storage=private_media.storages.PrivateMediaStorage(), upload_to=projects.models.screenshot_upload_to)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Page')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Platform')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='platform',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='page',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name_slug', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('name_slug', 'project')]),
        ),
    ]
