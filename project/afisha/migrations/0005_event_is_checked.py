# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_event_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
