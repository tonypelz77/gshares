# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0008_auto_20141119_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='wkH',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stock',
            name='wkL',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
