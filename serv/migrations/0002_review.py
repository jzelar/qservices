# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_id', models.IntegerField()),
                ('review_text', models.TextField()),
                ('review_date', models.CharField(max_length=20)),
                ('review_polarity', models.CharField(max_length=3)),
            ],
        ),
    ]