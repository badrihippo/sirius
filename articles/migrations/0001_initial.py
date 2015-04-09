# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=150, blank=True)),
                ('title_show', models.BooleanField(default=True, verbose_name=b'Display title')),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('edit_date', models.DateTimeField(null=True, blank=True)),
                ('part_number', models.IntegerField(default=0, blank=True)),
                ('part_name', models.CharField(max_length=150, blank=True)),
                ('content', models.TextField()),
                ('blurb', models.TextField(blank=True)),
                ('show_blurb', models.BooleanField(default=False, verbose_name=b'Show blurb in full article?')),
                ('footer', models.TextField(blank=True)),
                ('pages', models.CommaSeparatedIntegerField(max_length=30)),
            ],
            options={
                'get_latest_by': 'issue',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('description', models.TextField(default=b'<p>No description!</p>')),
                ('submission_instructions', models.TextField(blank=True)),
                ('icon_left', models.URLField(blank=True)),
                ('icon_right', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, blank=True)),
                ('tagline', models.CharField(max_length=150, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
