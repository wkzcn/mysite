# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 02:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_author'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='articles',
        ),
    ]
