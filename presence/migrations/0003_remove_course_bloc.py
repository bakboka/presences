# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0002_auto_20160809_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='bloc',
        ),
    ]
