# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userActivity', '0004_auto_20180419_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='logout',
            field=models.DateTimeField(),
        ),
    ]
