# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_blogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('url_slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statement', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('debate', models.ForeignKey(to='blog.Debate')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogentry',
            name='user',
        ),
        migrations.DeleteModel(
            name='blogEntry',
        ),
    ]
