# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rufirst', '0012_auto_20170628_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='/Users/zhaoyu/PycharmProjects/RuDjango/rufirst/media/default.jpg', upload_to='userphotos'),
        ),
    ]
