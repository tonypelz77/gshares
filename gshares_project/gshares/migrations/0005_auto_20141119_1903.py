# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0004_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='mktcap',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='revenue',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='wkH',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='wkL',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(unique=True, max_length=6),
            preserve_default=True,
        ),
    ]
