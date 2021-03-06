# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-17 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_kami'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kami',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kamiid', models.CharField(max_length=255, unique=True)),
                ('kamizhi', models.CharField(default='未找到，请等待十分钟或联系卖家', max_length=255)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '卡密',
                'verbose_name_plural': '卡密',
                'ordering': ['-c_time'],
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='kami',
        ),
        migrations.AddField(
            model_name='user',
            name='kamiid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.Kami', to_field='kamiid'),
            preserve_default=False,
        ),
    ]
