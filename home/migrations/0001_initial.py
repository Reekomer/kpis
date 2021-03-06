# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datepub', models.DateField(max_length=30, null=True)),
                ('page_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(unique=True, max_length=100)),
                ('reactions', models.IntegerField(null=True)),
                ('comments', models.IntegerField(null=True)),
                ('shares', models.IntegerField(null=True)),
                ('views', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datepub', models.DateField(max_length=30)),
                ('page_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(unique=True, max_length=100)),
                ('reactions', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('shares', models.IntegerField()),
                ('views', models.IntegerField()),
            ],
        ),
    ]
