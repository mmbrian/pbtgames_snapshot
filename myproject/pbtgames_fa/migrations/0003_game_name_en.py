# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbtgames_fa', '0002_game_preloader'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='name_en',
            field=models.CharField(default='barfak', max_length=144),
            preserve_default=False,
        ),
    ]
