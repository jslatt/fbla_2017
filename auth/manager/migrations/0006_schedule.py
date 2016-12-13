# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-12-09 18:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_remove_employee_hire_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeWorking', models.IntegerField(default=1)),
                ('dayWorking', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('half', models.TimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
