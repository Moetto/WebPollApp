# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilmoapp', '0014_auto_20160206_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectonequestion',
            name='widget',
            field=models.CharField(choices=[('default', 'default'), ('radio button', 'radio button')], default='default', max_length=20),
        ),
    ]
