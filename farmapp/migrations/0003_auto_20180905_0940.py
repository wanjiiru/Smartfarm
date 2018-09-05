# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-05 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0002_auto_20180905_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detect',
            name='disease',
        ),
        migrations.AddField(
            model_name='image',
            name='locality',
            field=models.TextField(default='Embu'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='detect',
        ),
    ]
