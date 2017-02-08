# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_idle',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88idle\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_iowait',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88iowait\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_irq',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88irq\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_nice',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88nice\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_softirq',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88softirq\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_steal',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88steal\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_system',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88system\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_per_user',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88user\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_percent_guest',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88guest\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cpuinfo',
            name='cpu_percent_guest_nice',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87\xef\xbc\x88guest_nice\xef\xbc\x89', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cpuinfo',
            name='cpu_count',
            field=models.IntegerField(default=0, verbose_name=b'CPU \xe4\xb8\xaa\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='cpuinfo',
            name='cpu_percent',
            field=models.DecimalField(default=0.0, verbose_name=b'CPU \xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87', max_digits=5, decimal_places=2),
        ),
    ]
