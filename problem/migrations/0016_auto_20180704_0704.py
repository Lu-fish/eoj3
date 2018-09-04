# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0015_auto_20180704_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='level',
            field=models.IntegerField(choices=[(1, 'Naive'), (2, 'Easy'), (3, 'Medium'), (4, 'Hard'), (5, 'Super')], default=3, verbose_name='Difficulty Level'),
        ),
    ]