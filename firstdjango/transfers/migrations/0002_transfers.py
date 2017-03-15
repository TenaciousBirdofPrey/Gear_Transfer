# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=10)),
                ('to_location', models.CharField(max_length=10)),
                ('item', models.CharField(max_length=20)),
            ],
        ),
    ]