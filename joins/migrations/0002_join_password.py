# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='password',
            field=models.CharField(default=datetime.date(2014, 10, 31), max_length=30),
            preserve_default=False,
        ),
    ]
