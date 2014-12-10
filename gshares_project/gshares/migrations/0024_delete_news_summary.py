# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0023_financial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News_Summary',
        ),
    ]
