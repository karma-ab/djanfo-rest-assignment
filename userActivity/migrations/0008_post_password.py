# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userActivity', '0007_auto_20180420_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(default=b'root', max_length=200),
        ),
    ]