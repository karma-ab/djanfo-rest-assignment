# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userActivity', '0003_auto_20180418_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
