# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0005_auto_20141119_1903'),
    ]

    operations = [
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
            name='revenue',
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
