# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20170727_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='texto',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
