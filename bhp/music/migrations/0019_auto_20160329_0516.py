# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_auto_20160329_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtube',
            name='release',
        ),
        migrations.AddField(
            model_name='youtube',
            name='track',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='music.Track'),
            preserve_default=False,
        ),
    ]
