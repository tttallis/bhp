# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 08:58
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_auto_20160329_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
