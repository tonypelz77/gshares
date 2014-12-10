# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(unique=True, max_length=7)),
                ('name', models.CharField(unique=True, max_length=25)),
                ('mktcap', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
