# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0011_news_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mktcap', models.IntegerField()),
                ('wkH', models.FloatField()),
                ('wkL', models.FloatField()),
                ('price', models.FloatField()),
                ('stock', models.ForeignKey(to='gshares.Stock')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='stock',
            name='mktcap',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='wkH',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='wkL',
        ),
    ]
