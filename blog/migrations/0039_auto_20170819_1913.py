# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-19 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20170819_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(max_length=50),
        ),
    ]
