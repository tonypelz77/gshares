# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0002_auto_20141118_2211'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='Ticker',
        ),
    ]
