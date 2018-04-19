# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=200)),
                ('logout', models.CharField(max_length=200)),
            ],
        ),
    ]