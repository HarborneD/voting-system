# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-15 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_system', '0005_finalcheck_test3'),
    ]

    operations = [
        migrations.CreateModel(
            name='finalCheck2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
            ],
        ),
    ]
