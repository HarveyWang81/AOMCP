# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0007_auto_20170123_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memoryinfo',
            name='swap_memory',
        ),
        migrations.RemoveField(
            model_name='memoryinfo',
            name='virtual_memory',
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='memory_available',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x86\x85\xe5\xad\x98\xe5\x8f\xaf\xe7\x94\xa8\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='memory_free',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x86\x85\xe5\xad\x98\xe7\xa9\xba\xe9\x97\xb2\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='memory_percent',
            field=models.DecimalField(default=0.0, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88%\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='memory_total',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='memory_used',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x86\x85\xe5\xad\x98\xe4\xbd\xbf\xe7\x94\xa8\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='swap_free',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa4\xe6\x8d\xa2\xe5\x8c\xba\xe5\x86\x85\xe5\xad\x98\xe7\xa9\xba\xe9\x97\xb2\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='swap_percent',
            field=models.DecimalField(default=0.0, verbose_name=b'\xe4\xba\xa4\xe6\x8d\xa2\xe5\x8c\xba\xe5\x86\x85\xe5\xad\x98\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88%\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='swap_total',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa4\xe6\x8d\xa2\xe5\x8c\xba\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='memoryinfo',
            name='swap_used',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa4\xe6\x8d\xa2\xe5\x8c\xba\xe5\x86\x85\xe5\xad\x98\xe4\xbd\xbf\xe7\x94\xa8\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AlterField(
            model_name='cpuinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 15:18:54', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AlterField(
            model_name='diskinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 15:18:54', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='disk_total',
            field=models.IntegerField(verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe5\xa4\xa7\xe5\xb0\x8f\xef\xbc\x88M\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='memory_total',
            field=models.IntegerField(verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f\xef\xbc\x88M\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='memoryinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 15:18:54', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AlterField(
            model_name='netinfo',
            name='insert_datetime',
            field=models.DateTimeField(default=b'2017-01-23 15:18:54', verbose_name=b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
    ]
