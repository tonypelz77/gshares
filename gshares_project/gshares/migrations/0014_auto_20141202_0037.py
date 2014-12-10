# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0013_auto_20141201_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financial',
            old_name='ticker',
            new_name='stock',
        ),
    ]
