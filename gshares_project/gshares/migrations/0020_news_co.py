# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0019_remove_news_summary_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Co',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=6)),
                ('link', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
