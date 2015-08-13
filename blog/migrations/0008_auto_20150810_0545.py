# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150809_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_image',
            field=models.ImageField(default='', upload_to=b'images/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
