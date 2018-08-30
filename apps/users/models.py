# _*_coding:utf-8_*_
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

# Create your models here.

########################################
# 部门
########################################

class UserDepartment(models.Model):
    department_id = models.CharField(verbose_name='部门ID', max_length=10)
    name = models.CharField(verbose_name='部门名称', max_length=50)
    desc = models.CharField(verbose_name='部门描述', max_length=200, blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


########################################
# 用户职位
########################################
class UserPosition(models.Model):
    position_id = models.CharField(verbose_name='职位ID', max_length=10)
    name = models.CharField(verbose_name='职位名称', max_length=20,)
    desc = models.CharField(verbose_name='职位描述', max_length=200, blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


########################################
# 用户模块
#员工ID	user_id	Char(10)	工号
#姓名	user_name	Char(10)	姓名
#职位	position	Char(10)	运维支持，培训
#状态	state	Char(1)	在职，离职
#帐号	Account	Char(20)	登录系统的帐号
#密码	Password	Char(20)	登录系统的密码
#创建时间	Create_time
########################################

class UserProfile(AbstractUser):
    user_id = models.CharField(verbose_name='员工ID',max_length=10,blank=True, null=True)
    user_name = models.CharField(verbose_name='员工姓名',max_length=10,blank=True, null=True)
    mobile = models.CharField(verbose_name='手机号码', max_length=20, blank=True, null=True)
    department = models.ForeignKey(UserDepartment, related_name='user_department',verbose_name='部门', blank=True, null=True)
    position = models.ForeignKey(UserPosition, related_name='user_position',verbose_name='职位', blank=True, null=True)
    desc = models.TextField(verbose_name='备注', blank=True, null=True)
    state = models.CharField(verbose_name='状态',max_length=1,default=1)
    account = models.CharField(verbose_name='账号',max_length=10,blank=True, null=True)
    password = models.CharField(verbose_name='密码',max_length=50,blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name ='用户1'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name

###############################################
## 用户登录信息表
###############################################

class UserLoginRecord(models.Model):
    user = models.ForeignKey(UserProfile, related_name='user_loginrecord',verbose_name='用户')
    agent = models.CharField(verbose_name='客户端', max_length=200, blank=True, null=True)
    city = models.CharField(verbose_name='登录区域', max_length=100, blank=True, null=True)
    ip = models.GenericIPAddressField(verbose_name='客户端IP', blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='登陆时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户登录信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username