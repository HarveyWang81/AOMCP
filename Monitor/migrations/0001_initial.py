# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_uid', models.CharField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe7\xa0\x81')),
                ('cpu_count', models.IntegerField(verbose_name=b'CPU \xe4\xb8\xaa\xe6\x95\xb0')),
                ('cpu_percent', models.DecimalField(verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87', max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='DiskInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_uid', models.CharField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe7\xa0\x81')),
                ('disk_usage', models.IntegerField(verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe7\x9a\x84\xe4\xbd\xbf\xe7\x94\xa8\xe6\x83\x85\xe5\x86\xb5')),
                ('disk_io_counters', models.IntegerField(verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe6\x95\xb4\xe4\xbd\x93\xe7\x9a\x84 I/O \xe6\x83\x85\xe5\x86\xb5')),
            ],
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_uid', models.CharField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe7\xa0\x81')),
                ('host_ip', models.CharField(max_length=15, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba IP \xe5\x9c\xb0\xe5\x9d\x80')),
                ('host_name', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('host_mac', models.CharField(max_length=17, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba MAC \xe5\x9c\xb0\xe5\x9d\x80')),
                ('os', models.CharField(max_length=10, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('memory_total', models.IntegerField(verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f\xef\xbc\x88kb\xef\xbc\x89')),
                ('disk_total', models.IntegerField(verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe5\xa4\xa7\xe5\xb0\x8f\xef\xbc\x88kb\xef\xbc\x89')),
            ],
        ),
        migrations.CreateModel(
            name='MemoryInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_uid', models.CharField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe7\xa0\x81')),
                ('virtual_memory', models.IntegerField(verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x86\x85\xe5\xad\x98\xe7\x9a\x84\xe4\xbd\xbf\xe7\x94\xa8\xe6\x83\x85\xe5\x86\xb5')),
                ('swap_memory', models.IntegerField(verbose_name=b'\xe4\xba\xa4\xe6\x8d\xa2\xe5\x8c\xba\xe5\x86\x85\xe5\xad\x98\xe7\x9a\x84\xe4\xbd\xbf\xe7\x94\xa8\xe6\x83\x85\xe5\x86\xb5')),
            ],
        ),
        migrations.CreateModel(
            name='NetInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_uid', models.CharField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe7\xa0\x81')),
                ('net_io_counters', models.IntegerField(verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe7\x9a\x84 I/O \xe6\x83\x85\xe5\x86\xb5')),
            ],
        ),
    ]
