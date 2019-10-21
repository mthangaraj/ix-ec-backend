# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_contact_espressocontact'),
        ('accounting', '0014_coamap_is_mapped'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickBookLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=20)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
        ),
    ]