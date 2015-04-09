# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150407_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sources',
            field=models.ManyToManyField(to='media.Source', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='articles.Tag', blank=True),
        ),
    ]
