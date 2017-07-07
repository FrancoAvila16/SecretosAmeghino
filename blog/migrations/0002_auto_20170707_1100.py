# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='post',
            name='chismes_de',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Alumno'), (b'P', b'Profesor'), (b'O', b'Otros')]),
        ),
    ]
