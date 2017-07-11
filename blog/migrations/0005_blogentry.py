# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20170707_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('blogText', models.TextField()),
                ('image', models.ImageField(upload_to='blogImgs/')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
