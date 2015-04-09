# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Squiggle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event1', models.CharField(max_length=128)),
                ('date1', models.DateField()),
                ('event2', models.CharField(max_length=128, blank=True)),
                ('date2', models.DateField(null=True, blank=True)),
                ('embed_code', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date1'],
            },
        ),
        migrations.CreateModel(
            name='UpcomingSquiggle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('last_date', models.DateField()),
                ('event_description', models.TextField(blank=True)),
            ],
        ),
    ]
