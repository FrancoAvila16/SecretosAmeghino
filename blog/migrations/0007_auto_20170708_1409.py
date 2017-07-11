# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20170708_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVotes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('vote_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='statement',
            name='debate',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Debate',
        ),
        migrations.DeleteModel(
            name='Statement',
        ),
        migrations.AddField(
            model_name='uservotes',
            name='post',
            field=models.ForeignKey(related_name='post_votes', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='uservotes',
            name='user',
            field=models.ForeignKey(related_name='user_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='uservotes',
            unique_together=set([('user', 'post', 'vote_type')]),
        ),
    ]
