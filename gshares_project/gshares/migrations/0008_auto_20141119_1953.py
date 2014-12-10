# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0007_auto_20141119_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='revenue',
        ),
        migrations.AlterField(
            model_name='stock',
            name='mktcap',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='wkH',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='wkL',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
