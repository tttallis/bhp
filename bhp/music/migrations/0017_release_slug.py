# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 09:13
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_release_cover_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
