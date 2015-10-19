# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('misc', '0002_auto_20150808_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager_type', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Primary'), (b'S', b'Secondary')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('photo', models.ImageField(null=True, upload_to=b'media/%Y/%m/%d', blank=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mer_name', models.CharField(max_length=255, null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'O_UA', max_length=4, choices=[(b'M_A', b'Approved'), (b'M_UA', b'Unapproved')])),
                ('is_verified', models.BooleanField(default=False)),
                ('merchant_type', models.CharField(max_length=3, choices=[(b'LIC', b'Licensed'), (b'GOV', b'Goverment Funded'), (b'PER', b'Personal Licensed Merchant')])),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('mer_website', models.CharField(max_length=255, null=True, blank=True)),
                ('logo', models.ImageField(default=None, null=True, upload_to=b'media/%Y/%m/%d', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('phoneno', models.CharField(max_length=11, null=True, blank=True)),
                ('address1', models.CharField(max_length=255, null=True, blank=True)),
                ('address2', models.CharField(max_length=255, null=True, blank=True)),
                ('pincode', models.CharField(max_length=6, null=True, blank=True)),
                ('address_verified', models.BooleanField(default=False)),
                ('city', models.ForeignKey(related_name=b'office city mer+', blank=True, to='misc.City', null=True)),
                ('org', models.ForeignKey(blank=True, to='merchant.Merchant', null=True)),
                ('place', models.ForeignKey(related_name=b'office area mer+', blank=True, to='misc.Place', null=True)),
                ('state', models.ForeignKey(related_name=b'office state mer+', blank=True, to='misc.State', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='managers',
            name='merchant',
            field=models.ForeignKey(blank=True, to='merchant.Merchant', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='managers',
            name='user',
            field=models.OneToOneField(related_name=b'user_mer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
