# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('rate_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_id', models.IntegerField()),
                ('rate_polarity', models.CharField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='service',
            name='category_id',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
    ]