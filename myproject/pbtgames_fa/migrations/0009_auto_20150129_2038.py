# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbtgames_fa', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desc_fa',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name_fa',
            field=models.CharField(default='', max_length=144),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='title_fa',
            field=models.CharField(default='', max_length=144),
            preserve_default=False,
        ),
    ]
