# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_release__artist_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='label',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.Label'),
            preserve_default=False,
        ),
    ]