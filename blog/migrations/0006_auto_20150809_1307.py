# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150806_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created'], 'verbose_name': 'blog post', 'verbose_name_plural': 'blog posts'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='body_html',
            field=models.TextField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 9, 11, 7, 38, 336516, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
