# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRegistration', '0013_auto_20170807_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymdetails',
            name='gymImage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
