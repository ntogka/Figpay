# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='url',
        ),
    ]
