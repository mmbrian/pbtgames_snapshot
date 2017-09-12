# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbtgames_fa', '0005_auto_20150101_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='portrait_only',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
