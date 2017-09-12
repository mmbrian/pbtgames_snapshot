# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbtgames_fa', '0004_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='allowed_on_en',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='overview_en',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='premier_description_en',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='premier_title_en',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='overview_en',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='title_en',
            field=models.CharField(default='', max_length=144, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='name_en',
            field=models.CharField(max_length=144, blank=True),
            preserve_default=True,
        ),
    ]
