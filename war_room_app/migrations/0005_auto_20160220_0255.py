# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('war_room_app', '0004_auto_20160220_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='war_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='war',
            name='size',
            field=models.IntegerField(choices=[(10, '10 Vs 10'), (15, '15 Vs 15'), (20, '20 Vs 20'), (25, '25 Vs 25'), (30, '30 Vs 30'), (35, '35 Vs 35'), (40, '40 Vs 40'), (45, '45 Vs 45'), (50, '50 Vs 50')], default=10),
        ),
    ]
