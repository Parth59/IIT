# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160512164014 on 2016-06-14 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nettest', '0005_testsim2_dest'),
    ]

    operations = [
        migrations.CreateModel(
            name='monicaldown1',
            fields=[
                ('id2', models.AutoField(primary_key=True, serialize=False)),
                ('ips2', models.CharField(blank=True, max_length=50, null=True)),
                ('ipd2', models.CharField(blank=True, max_length=50, null=True)),
                ('packetsumdown', models.IntegerField(blank=True, null=True)),
                ('sum2', models.IntegerField(blank=True, null=True)),
                ('mean2', models.FloatField(blank=True, null=True)),
                ('banddown', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='monicalup1',
            fields=[
                ('id1', models.AutoField(primary_key=True, serialize=False)),
                ('ips1', models.CharField(blank=True, max_length=50, null=True)),
                ('ipd1', models.CharField(blank=True, max_length=50, null=True)),
                ('packetsumup', models.IntegerField(blank=True, null=True)),
                ('sum1', models.IntegerField(blank=True, null=True)),
                ('mean1', models.FloatField(blank=True, null=True)),
                ('bandup', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]