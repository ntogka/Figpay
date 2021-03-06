# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='profiles.Consumer')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Vendor')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.PointOfSale'),
        ),
    ]
