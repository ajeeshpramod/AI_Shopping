# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-27 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20210116_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trouble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=200)),
                ('trouble', models.CharField(max_length=200)),
                ('solution', models.CharField(max_length=200)),
            ],
        ),
    ]
