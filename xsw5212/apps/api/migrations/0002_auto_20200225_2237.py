# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-25 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='word_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
