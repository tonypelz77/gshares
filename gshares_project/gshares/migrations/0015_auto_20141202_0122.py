# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0014_auto_20141202_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial',
            name='stock',
        ),
        migrations.DeleteModel(
            name='Financial',
        ),
    ]
