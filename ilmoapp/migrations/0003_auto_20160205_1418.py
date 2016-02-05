# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ilmoapp', '0002_auto_20160205_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectOneQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ilmoapp.Question')),
                ('answer', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('ilmoapp.question',),
        ),
        migrations.AlterField(
            model_name='textquestion',
            name='answer',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
