# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_publisher_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='update',
            field=models.DateTimeField(null=True),
        ),
    ]
