# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 09:23
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_auto_20160329_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='soundcloud',
            field=embed_video.fields.EmbedVideoField(default=''),
            preserve_default=False,
        ),
    ]
