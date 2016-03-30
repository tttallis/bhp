# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0022_track_soundcloud'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('alpha_name',)},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='release',
            name='blurb',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='artists',
            field=models.ManyToManyField(related_name='releases', to='music.Artist'),
        ),
    ]