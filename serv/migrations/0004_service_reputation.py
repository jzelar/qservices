# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0003_auto_20181103_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='reputation',
            field=models.FloatField(default=0.0),
        ),
    ]
