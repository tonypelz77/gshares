# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0021_auto_20141204_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial',
            name='stock',
        ),
        migrations.DeleteModel(
            name='Financial',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
