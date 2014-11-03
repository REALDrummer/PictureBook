# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20141031_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='email2',
            field=models.EmailField(default='none', max_length=75),
            preserve_default=False,
        ),
    ]
