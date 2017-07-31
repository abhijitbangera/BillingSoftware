# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appRegistration', '0005_gymplans'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffDetails',
            fields=[
                ('staffName', models.CharField(max_length=100)),
                ('staffCity', models.CharField(max_length=100)),
                ('staffAddress', models.TextField(blank=True)),
                ('staffPincode', models.IntegerField(blank=True, max_length=9)),
                ('staffContactNumber', models.IntegerField(max_length=14)),
                ('staffEmergencyNumber', models.IntegerField(blank=True, max_length=14)),
                ('staffEmail', models.CharField(max_length=100)),
                ('staffRegistrationDate', models.DateTimeField(verbose_name='Registration Date')),
                ('staffNumber', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('staffStatus', models.BooleanField(default=True)),
                ('staffGymNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistration.gymDetails')),
            ],
        ),
    ]
