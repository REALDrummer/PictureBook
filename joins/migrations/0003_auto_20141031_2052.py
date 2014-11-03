# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_join_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='pTimestamp',
            field=models.DateTimeField(default=datetime.date(2014, 10, 31), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='join',
            name='pUpdated',
            field=models.DateTimeField(default=datetime.date(2014, 10, 31), auto_now=True),
            preserve_default=False,
        ),
    ]
