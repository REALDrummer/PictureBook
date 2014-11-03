# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0005_join_email2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='email2',
        ),
        migrations.AddField(
            model_name='join',
            name='password',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
