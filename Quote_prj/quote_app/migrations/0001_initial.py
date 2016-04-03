# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quote', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
    ]
