# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170707_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
