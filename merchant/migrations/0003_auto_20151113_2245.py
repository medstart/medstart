# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_auto_20150809_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='org',
            new_name='mer',
        ),
        migrations.RemoveField(
            model_name='office',
            name='email',
        ),
    ]
