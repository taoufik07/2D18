# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-25 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171225_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='sponsor_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='sponsor_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]