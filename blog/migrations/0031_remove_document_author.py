# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-28 23:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_document_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
    ]