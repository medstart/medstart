# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='status',
            field=models.CharField(default=b'M_UA', max_length=4, choices=[(b'M_A', b'Approved'), (b'M_UA', b'Unapproved')]),
        ),
    ]
