# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilmoapp', '0012_auto_20160205_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
