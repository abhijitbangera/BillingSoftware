# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRegistration', '0010_auto_20170805_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymdetails',
            name='gymType',
            field=models.CharField(choices=[('gym', 'Gym'), ('yoga', 'Yoga')], max_length=100),
        ),
    ]
