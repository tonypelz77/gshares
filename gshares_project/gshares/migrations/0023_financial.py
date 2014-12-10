# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0022_auto_20141204_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(unique=True, max_length=6)),
                ('name', models.CharField(max_length=50)),
                ('mktcap', models.IntegerField()),
                ('wkH', models.FloatField()),
                ('wkL', models.FloatField()),
                ('price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
