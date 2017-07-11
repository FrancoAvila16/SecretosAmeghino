# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20170707_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='chismes_de',
            field=models.CharField(choices=[('A', 'Alumno'), ('P', 'Profesor'), ('O', 'Otros')], max_length=1, default='A'),
        ),
    ]
