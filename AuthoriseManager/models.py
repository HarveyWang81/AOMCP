#coding:utf-8

from django.db import models

class User(models.Model):
    user_code = models.CharField(max_length=30, verbose_name='用户ID')
    user_name = models.CharField(max_length=30, verbose_name='用户全名', blank=True, null=True)
    password = models.CharField(max_length=30, verbose_name='用户密码')
    e_mail = models.EmailField(verbose_name='邮箱地址', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='用户手机', blank=True, null=True)
    photo = models.ImageField(upload_to='image/userphoto', verbose_name='用户头像', blank=True, null=True)


class Group(models.Model):
    group_name = models.CharField(max_length=30, verbose_name='分组名称')

