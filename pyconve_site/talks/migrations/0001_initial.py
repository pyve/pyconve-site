# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('talk_type', models.IntegerField(verbose_name='Type', choices=[(1, 'Talk'), (2, 'Workshop')])),
                ('short_description', models.TextField(verbose_name='Description')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
