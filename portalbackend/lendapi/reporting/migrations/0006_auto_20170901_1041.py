# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='download',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]