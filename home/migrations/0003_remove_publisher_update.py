# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_publisher_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='update',
        ),
    ]
