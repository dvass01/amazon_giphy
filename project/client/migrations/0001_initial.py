# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import client.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(validators=[client.models.Client.validate_name], unique=True, max_length=255)),
                ('password', models.CharField(validators=[client.models.Client.validate_password], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
