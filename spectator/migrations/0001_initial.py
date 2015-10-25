# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('provider', models.CharField(max_length=200)),
                ('configuration', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(null=True, upload_to=b'')),
                ('source', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('cover', models.ImageField(null=True, upload_to=b'')),
                ('genre', models.CharField(max_length=100, blank=True)),
                ('show_type', models.CharField(max_length=100, blank=True)),
                ('channel', models.ForeignKey(to='spectator.Channel')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='show',
            field=models.ForeignKey(to='spectator.Show'),
        ),
    ]
