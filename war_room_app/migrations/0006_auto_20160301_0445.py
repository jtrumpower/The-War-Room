# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('war_room_app', '0005_auto_20160220_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
