# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-14 18:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_auto_20170603_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyplan',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 14, 21, 12, 36, 426520)),
        ),
        migrations.AlterField(
            model_name='product',
            name='dt',
            field=models.DateField(default=datetime.datetime(2017, 6, 17, 21, 12, 36, 422517)),
        ),
        migrations.AlterField(
            model_name='recipepart',
            name='tm',
            field=models.TimeField(default=datetime.datetime(2017, 6, 14, 21, 12, 36, 426520)),
        ),
        migrations.AlterField(
            model_name='remainportion',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 14, 21, 12, 36, 422517)),
        ),
    ]
