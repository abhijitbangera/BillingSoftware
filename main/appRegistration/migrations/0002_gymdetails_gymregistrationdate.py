# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appRegistration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymdetails',
            name='gymRegistrationDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration Date'),
            preserve_default=False,
        ),
    ]
