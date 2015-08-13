# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150810_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description_image',
            field=models.ImageField(upload_to=b'images/%Y/%m/%d/'),
        ),
    ]
