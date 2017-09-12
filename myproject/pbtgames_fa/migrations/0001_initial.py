# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addition_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=144)),
                ('release_date', models.DateTimeField()),
                ('overview', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('is_premiered', models.BooleanField(default=True)),
                ('premier_title', models.TextField(blank=True)),
                ('premier_description', models.TextField(blank=True)),
                ('premier_image', models.ImageField(upload_to=b'premier_images/', blank=True)),
                ('icon', models.ImageField(upload_to=b'icons/')),
                ('googleplay_link', models.CharField(max_length=300, blank=True)),
                ('appstore_link', models.CharField(max_length=300, blank=True)),
                ('bazaar_link', models.CharField(max_length=300, blank=True)),
                ('sibche_link', models.CharField(max_length=300, blank=True)),
                ('windows_link', models.CharField(max_length=300, blank=True)),
                ('mac_link', models.CharField(max_length=300, blank=True)),
                ('linux_link', models.CharField(max_length=300, blank=True)),
                ('facebook_like_embedded_link', models.TextField(blank=True)),
                ('googleplus_embedded_link', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScreenShot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=144, blank=True)),
                ('overview', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'screenshots/')),
                ('game', models.ForeignKey(related_name='screenshots', to='pbtgames_fa.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
