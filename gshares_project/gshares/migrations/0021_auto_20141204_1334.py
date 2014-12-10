# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0020_news_co'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterField(
            model_name='news_co',
            name='title',
            field=models.CharField(unique=True, max_length=300),
            preserve_default=True,
        ),
    ]
