# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 06:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20180202_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='secret_key',
            field=models.TextField(default='', help_text='Copy and paste your private key for Xero Private company', validators=[django.core.validators.MinLengthValidator(10, message='Atleast 10 characters required')]),
        ),
    ]
