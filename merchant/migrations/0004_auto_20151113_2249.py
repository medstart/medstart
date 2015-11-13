# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0003_auto_20151113_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='mobile',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='merchant',
            name='phoneno',
            field=models.CharField(max_length=11, null=True, blank=True),
            preserve_default=True,
        ),
    ]
