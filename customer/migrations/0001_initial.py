# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30, db_index=True)),
                ('last_name', models.CharField(max_length=30, db_index=True)),
                ('gender', models.CharField(default=None, choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1, blank=True, null=True, db_index=True)),
                ('status', models.CharField(default=b'R', max_length=3, blank=True, choices=[(b'R', b'Registered'), (b'RET', b'Returning')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('customer_id', models.OneToOneField(primary_key=True, serialize=False, to='customer.Customer', verbose_name=b'customer id')),
                ('current_address1', models.CharField(max_length=255, null=True, blank=True)),
                ('current_address2', models.CharField(max_length=255, null=True, blank=True)),
                ('current_pincode', models.CharField(max_length=6, null=True, blank=True)),
                ('place', models.ForeignKey(verbose_name=b'place name', blank=True, to='misc.Place', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('customer_id', models.OneToOneField(primary_key=True, serialize=False, to='customer.Customer', verbose_name=b'customer id')),
                ('del_address1', models.CharField(max_length=255, null=True, blank=True)),
                ('del_address2', models.CharField(max_length=255, null=True, blank=True)),
                ('del_pincode', models.CharField(max_length=6, null=True, blank=True)),
                ('place', models.ForeignKey(verbose_name=b'place name', blank=True, to='misc.Place', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='customer',
            name='source',
            field=models.ForeignKey(related_name=b'source_of_data', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(related_name=b'customer_user', null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
