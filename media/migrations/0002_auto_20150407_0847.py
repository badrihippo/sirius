# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='illustrators',
            field=models.ManyToManyField(to='people.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='sources',
            field=models.ManyToManyField(to='media.Source', blank=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='copyrights',
            field=models.ManyToManyField(to='media.Copyright', blank=True),
        ),
    ]
