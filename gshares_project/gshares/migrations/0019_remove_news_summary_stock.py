# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0018_auto_20141202_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_summary',
            name='stock',
        ),
    ]
