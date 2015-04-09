# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        ('issue', '0002_auto_20150407_0821'),
        ('people', '__first__'),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='header_image',
            field=models.ForeignKey(blank=True, to='media.Picture', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.ForeignKey(blank=True, to='media.Picture', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(blank=True, to='issue.Issue', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='persons',
            field=models.ManyToManyField(to='people.Person'),
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(to='articles.Section'),
        ),
        migrations.AddField(
            model_name='article',
            name='series',
            field=models.ForeignKey(blank=True, to='articles.Series', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sources',
            field=models.ManyToManyField(to='media.Source', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='articles.Tag', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ForeignKey(related_name='article_thumbnail', blank=True, to='media.Picture', null=True),
        ),
    ]
