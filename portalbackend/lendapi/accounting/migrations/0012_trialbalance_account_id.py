# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_auto_20170823_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialbalance',
            name='account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
