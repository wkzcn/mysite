# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_remove_comment_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
