# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0002_auto_20180927_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pub_date',
        ),
    ]
