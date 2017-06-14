# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('article_summary', models.TextField()),
                ('article_body', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('view_times', models.IntegerField()),
            ],
        ),
    ]
