# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('name', models.CharField(max_length=30, blank=True)),
                ('shortname', models.SlugField(serialize=False, primary_key=True)),
                ('image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disp_title', models.CharField(max_length=256, blank=True)),
                ('caption', models.CharField(max_length=300, blank=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'smedia', blank=True)),
                ('credit', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('illustrators', models.ManyToManyField(to='people.Person', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(blank=True)),
                ('detail', models.TextField(blank=True)),
                ('icon', models.URLField(blank=True)),
                ('sss_copyright', models.BooleanField(default=False)),
                ('copyrights', models.ManyToManyField(to='media.Copyright', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='sources',
            field=models.ManyToManyField(to='media.Source', null=True, blank=True),
        ),
    ]
