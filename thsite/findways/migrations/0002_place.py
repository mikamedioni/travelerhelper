# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findways', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
    ]
