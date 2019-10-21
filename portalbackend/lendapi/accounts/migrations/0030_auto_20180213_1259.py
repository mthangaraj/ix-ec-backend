# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-13 12:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20180212_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounting_type', models.CharField(choices=[('quickbooks', 'Quickbooks'), ('xero', 'Xero'), ('sage', 'Sage')], default='quickbooks', max_length=60)),
                ('xero_accounting_type', models.CharField(blank=True, choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private'), ('PARTNER', 'Partner')], max_length=50, null=True)),
                ('auth_key', models.CharField(blank=True, max_length=500, null=True, validators=[django.core.validators.MinLengthValidator(10, message='Atleast 10 characters required')])),
                ('secret_key', models.TextField(blank=True, help_text='Copy & paste the rsa key content from generated .pem for xero private type accounting access. Otherwise secret key required.', null=True, validators=[django.core.validators.MinLengthValidator(10, message='Atleast 10 characters required')])),
            ],
            options={
                'db_table': 'accountingconfiguration',
            },
        ),
        migrations.RemoveField(
            model_name='companyaccountingconfiguration',
            name='company',
        ),
        migrations.DeleteModel(
            name='CompanyAccountingConfiguration',
        ),
    ]