# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='email',
            field=models.EmailField(default='noreply@ve.pycon.org', max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='talk',
            name='speaker_name',
            field=models.CharField(default='Speaker Name', max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
