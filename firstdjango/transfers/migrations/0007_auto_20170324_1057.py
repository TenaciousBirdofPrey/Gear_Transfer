# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0006_transfers_pick_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='pick_date',
            field=models.DateField(verbose_name='return date'),
        ),
    ]