# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 08:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0003_remove_course_bloc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]