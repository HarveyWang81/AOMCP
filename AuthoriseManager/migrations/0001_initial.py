# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=30, verbose_name=b'\xe5\x88\x86\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_code', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID')),
                ('user_name', models.CharField(max_length=30, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x85\xa8\xe5\x90\x8d', blank=True)),
                ('password', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('e_mail', models.EmailField(max_length=254, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x89\x8b\xe6\x9c\xba', blank=True)),
                ('photo', models.ImageField(upload_to=b'image/userphoto', null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
            ],
        ),
    ]
