# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nettest', '0014_remove_monitable_monid'),
    ]

    operations = [
        migrations.CreateModel(
            name='percentageofpacketdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monid1', models.CharField(blank=True, max_length=200, null=True)),
                ('pcid', models.CharField(blank=True, max_length=200, null=True)),
                ('ips1', models.CharField(blank=True, max_length=50, null=True)),
                ('p1_p500', models.IntegerField(blank=True, null=True)),
                ('p501_p1000', models.IntegerField(blank=True, null=True)),
                ('p1001_p2000', models.IntegerField(blank=True, null=True)),
                ('p2001', models.IntegerField(blank=True, null=True)),
                ('totdown', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='percentageofpacketup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monid1', models.CharField(blank=True, max_length=200, null=True)),
                ('pcid', models.CharField(blank=True, max_length=200, null=True)),
                ('ips1', models.CharField(blank=True, max_length=50, null=True)),
                ('p1_p500', models.IntegerField(blank=True, null=True)),
                ('p501_p1000', models.IntegerField(blank=True, null=True)),
                ('p1001_p2000', models.IntegerField(blank=True, null=True)),
                ('p2001', models.IntegerField(blank=True, null=True)),
                ('totup', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='monicaldown1',
        ),
        migrations.DeleteModel(
            name='monicalup1',
        ),
        migrations.AddField(
            model_name='monitable',
            name='monid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='monitable',
            name='pcid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
