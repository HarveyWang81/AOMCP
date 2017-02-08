# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0002_auto_20170122_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpuinfo',
            old_name='cpu_percent_guest',
            new_name='cpu_per_guest',
        ),
        migrations.RenameField(
            model_name='cpuinfo',
            old_name='cpu_percent_guest_nice',
            new_name='cpu_per_guest_nice',
        ),
    ]
