# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_auto_20150407_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squiggle',
            name='related_articles',
            field=models.ManyToManyField(to='articles.Article', blank=True),
        ),
        migrations.AlterField(
            model_name='squiggle',
            name='tags',
            field=models.ManyToManyField(to='articles.Tag', blank=True),
        ),
    ]
