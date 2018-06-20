# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialbalance',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company'),
        ),
        migrations.AddField(
            model_name='coamap',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company'),
        ),
        migrations.AddField(
            model_name='coa',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company'),
        ),
        migrations.AddField(
            model_name='accountingoauth2',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company'),
        ),
    ]
