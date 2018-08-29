# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-24 07:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0005_merge_20180822_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='detect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('Image', models.ImageField(upload_to='gross')),
                ('control', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('symptoms', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
        migrations.AddField(
            model_name='detect',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.Diseases'),
        ),
    ]