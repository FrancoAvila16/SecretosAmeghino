# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-24 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170722_2028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Excursion',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
