# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20141031_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='pTimestamp',
        ),
        migrations.RemoveField(
            model_name='join',
            name='pUpdated',
        ),
        migrations.RemoveField(
            model_name='join',
            name='password',
        ),
    ]
