# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0025_auto_20171018_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialstatemententrytag',
            name='tag_group',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]