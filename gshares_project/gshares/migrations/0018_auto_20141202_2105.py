# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0017_news_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news_summary',
            old_name='published',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='news_summary',
            name='summary',
        ),
    ]
