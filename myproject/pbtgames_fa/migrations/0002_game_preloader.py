# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pbtgames_fa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='preloader',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'preloaders/'),
            preserve_default=True,
        ),
    ]
