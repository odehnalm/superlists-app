# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='list',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
