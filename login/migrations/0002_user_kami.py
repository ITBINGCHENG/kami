# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-17 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kami',
            field=models.CharField(default='未找到，请等待十分钟或联系卖家', max_length=255),
        ),
    ]
