# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_acimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='site_changyan',
            field=models.TextField(default='', verbose_name='畅言评论代码'),
        ),
    ]
