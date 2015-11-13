# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0004_auto_20151113_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='merchant_type',
            field=models.CharField(default=b'LIC', max_length=3, choices=[(b'LIC', b'Licensed'), (b'GOV', b'Goverment Funded'), (b'PER', b'Personal Licensed Merchant')]),
        ),
    ]
