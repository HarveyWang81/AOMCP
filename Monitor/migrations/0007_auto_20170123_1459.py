# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0006_auto_20170123_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='diskinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 14:59:57', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 14:59:57', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AddField(
            model_name='netinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 14:59:57', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AlterField(
            model_name='cpuinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 14:59:57', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
    ]
