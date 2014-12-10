# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0006_auto_20141119_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='mktcap',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='revenue',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='wkH',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='wkL',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
