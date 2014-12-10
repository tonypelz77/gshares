# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshares', '0015_auto_20141202_0122'),
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
    ]
