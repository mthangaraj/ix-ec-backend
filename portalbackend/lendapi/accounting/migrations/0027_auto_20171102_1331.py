# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0026_financialstatemententrytag_tag_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coamap',
            options={'ordering': ('cust_account_name',), 'verbose_name': 'Chart of Accounts Map'},
        ),
    ]
