# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20171121_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
