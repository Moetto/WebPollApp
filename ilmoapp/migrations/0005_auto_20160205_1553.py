# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilmoapp', '0004_questionform_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionForm',
            new_name='Questionnaire',
        ),
    ]
