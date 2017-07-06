# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0014_auto_20170625_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailyplan',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 25, 16, 48, 46, 155478)),
        ),
        migrations.AlterField(
            model_name='recipepart',
            name='tm',
            field=models.TimeField(default=datetime.datetime(2017, 6, 25, 16, 48, 46, 154977)),
        ),
        migrations.AlterField(
            model_name='remainportion',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 25, 16, 48, 46, 150474)),
        ),
    ]