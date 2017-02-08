# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0003_auto_20170122_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_guest',
        ),
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_guest_nice',
        ),
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_iowait',
        ),
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_irq',
        ),
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_nice',
        ),
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_softirq',
        ),
        migrations.RemoveField(
            model_name='cpuinfo',
            name='cpu_per_steal',
        ),
    ]
