# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, to='misc.State', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='city',
            field=models.ForeignKey(blank=True, to='misc.City', null=True),
            preserve_default=True,
        ),
    ]
