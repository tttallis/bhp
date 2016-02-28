# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20160227_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('duration', models.CharField(blank=True, max_length=8, null=True)),
                ('position', models.CharField(blank=True, max_length=8, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Release')),
            ],
        ),
    ]
