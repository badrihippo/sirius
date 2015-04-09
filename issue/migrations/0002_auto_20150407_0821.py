# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0001_initial'),
        ('media', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squiggle',
            name='picture',
            field=models.ForeignKey(to='media.Picture'),
        ),
        migrations.AddField(
            model_name='squiggle',
            name='related_articles',
            field=models.ManyToManyField(to='articles.Article', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='squiggle',
            name='tags',
            field=models.ManyToManyField(to='articles.Tag', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='cover_article',
            field=models.OneToOneField(related_name='cover_article', null=True, blank=True, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='issue',
            name='cover_picture',
            field=models.ForeignKey(to='media.Picture'),
        ),
        migrations.AddField(
            model_name='issue',
            name='sections',
            field=models.ManyToManyField(to='articles.Section'),
        ),
        migrations.AddField(
            model_name='issue',
            name='squiggle',
            field=models.ForeignKey(blank=True, to='issue.Squiggle', null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='issue',
            field=models.ForeignKey(to='issue.Issue'),
        ),
    ]
