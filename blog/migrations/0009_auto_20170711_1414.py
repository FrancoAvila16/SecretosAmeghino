# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170708_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='chismes_de',
            field=models.CharField(default=b'Alumno', max_length=20, choices=[(b'Alumno', b'Alumno'), (b'Profesor', b'Profesor'), (b'Otros', b'Otros')]),
        ),
    ]
