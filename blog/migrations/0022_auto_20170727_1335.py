# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-27 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170727_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='archivo',
        ),
    ]
