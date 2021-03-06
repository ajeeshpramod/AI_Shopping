# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-06-07 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.CharField(default='5', max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
