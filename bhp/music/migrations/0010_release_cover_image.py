# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='cover_image',
            field=models.ImageField(default='', upload_to='covers'),
            preserve_default=False,
        ),
    ]
