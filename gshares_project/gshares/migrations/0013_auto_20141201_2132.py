# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0012_auto_20141201_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financial',
            old_name='stock',
            new_name='ticker',
        ),
    ]
