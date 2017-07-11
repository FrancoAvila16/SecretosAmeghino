# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170708_1409'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='uservotes',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='uservotes',
            name='post',
        ),
        migrations.RemoveField(
            model_name='uservotes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
        migrations.DeleteModel(
            name='UserVotes',
        ),
    ]
