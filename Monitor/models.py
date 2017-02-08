# coding:utf-8
import datetime
from django.db import models


class HostInfo(models.Model):
    """
    记录主机静态信息
    """
    host_uid = models.CharField(max_length=10, verbose_name='随机码')  # 随机编码，当第一次发数据给服务器时，由客户端自动生成
    host_ip = models.CharField(max_length=15, verbose_name='主机 IP 地址')
    host_name = models.CharField(max_length=100, verbose_name='主机名')
    host_mac = models.CharField(max_length=17, verbose_name='主机 MAC 地址')
    os = models.CharField(max_length=10, verbose_name='操作系统类型')
    memory_total = models.IntegerField(verbose_name='内存大小（M）')
    disk_total = models.IntegerField(verbose_name='硬盘大小（M）')


class CPUInfo(models.Model):
    """
    记录主机 CPU 动态性能信息
    """
    host_uid = models.CharField(max_length=10, verbose_name='随机码')
    insert_datetime = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                           , verbose_name='插入时间戳')
    cpu_count = models.IntegerField(default=0, verbose_name='CPU 个数')
    cpu_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name='CPU 使用率')
    cpu_per_user = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name='CPU 使用率（user）')
    cpu_per_system = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name='CPU 使用率（system）')
    cpu_per_idle = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name='CPU 使用率（idle）')


class MemoryInfo(models.Model):
    """
    记录主机内存动态性能信息
    """
    host_uid = models.CharField(max_length=10, verbose_name='随机码')
    insert_datetime = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                           , verbose_name='插入时间戳')
    memory_total = models.IntegerField(default=0, verbose_name='物理内存大小')
    memory_available = models.IntegerField(default=0, verbose_name='物理内存可用大小')
    memory_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name='内存使用率（%）')
    memory_used = models.IntegerField(default=0, verbose_name='物理内存使用大小')
    memory_free = models.IntegerField(default=0, verbose_name='物理内存空闲大小')
    swap_total = models.IntegerField(default=0, verbose_name='交换区内存大小')
    swap_used = models.IntegerField(default=0, verbose_name='交换区内存使用大小')
    swap_free = models.IntegerField(default=0, verbose_name='交换区内存空闲大小')
    swap_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name='交换区内存使用率（%）')


class DiskInfo(models.Model):
    """
    记录主机硬盘动态性能信息
    """
    host_uid = models.CharField(max_length=10, verbose_name='随机码')
    insert_datetime = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                           , verbose_name='插入时间戳')
    disk_usage = models.IntegerField(verbose_name='磁盘的使用情况')
    disk_io_counters = models.IntegerField(verbose_name='磁盘整体的 I/O 情况')


class NetInfo(models.Model):
    """
    记录主机网络动态性能信息
    """
    host_uid = models.CharField(max_length=10, verbose_name='随机码')
    insert_datetime = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                           , verbose_name='插入时间戳')
    net_io_counters = models.IntegerField(verbose_name='网络的 I/O 情况')
