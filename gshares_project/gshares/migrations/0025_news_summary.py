# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0024_delete_news_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('link', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
