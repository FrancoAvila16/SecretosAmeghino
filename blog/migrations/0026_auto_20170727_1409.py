# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-27 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_document_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='titulo',
            field=models.CharField(max_length=20),
        ),
    ]
