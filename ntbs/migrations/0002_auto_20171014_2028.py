# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntbook',
            name='meta',
            field=models.TextField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='ntbook',
            name='name',
            field=models.TextField(max_length=2048),
        ),
    ]
