# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160128_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='IP_addresses',
        ),
    ]
