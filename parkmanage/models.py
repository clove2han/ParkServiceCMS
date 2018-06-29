# _*_coding:utf-8_*_
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

import sys

# Create your models here.
EMPLOYEE_STATE =(
    ('在职','在职'),
    ('离职','离职'),
    ('其他','其他'),
)

class Employee(models.Model):
    # 员工ID
    employee_id = models.CharField(max_length=10, verbose_name='工号')
    # 姓名
    employee_name = models.CharField(max_length=20, verbose_name='姓名')
    # 职位
    position = models.CharField(max_length=20, verbose_name='职位')
    state = models.CharField(max_length=10,default='在职', verbose_name='状态')
    username = models.CharField(max_length=20,verbose_name='登陆账号')
    password = models.CharField(max_length=20,verbose_name='密码')

    # 创建员工的时间,默认为现在时间。

    create_time = models.DateTimeField(default=timezone.now,verbose_name='创建时间')

    # 此设置是说员工的显示顺序要按照employee_id的顺序来执行
    class Meta:
        ordering = ('employee_id',)
        verbose_name = u'员工表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.employee_id

PROVINCE = (
    ('广东省', '广东省'),
    ('湖北省', '湖北省'),
    ('四川省', '四川省'),
    ('云南省', '云南省'),
)

PARK_TYPE =(
    ('住宅','住宅'),
    ('写字楼','写字楼'),
    ('商业','商业'),
    ('商住混合','商住混合'),
)
# 停车场基本信息表
class Parkinfo(models.Model):
    park_id = models.CharField(max_length=30, verbose_name='停车场ID')
    park_name = models.CharField(max_length=50, verbose_name='停车场名称')
    country = models.CharField(blank=True, null=True,max_length=20, verbose_name='国家')
    province = models.CharField(blank=True, null=True,max_length=20, verbose_name='省')
    city = models.CharField(blank=True, null=True,max_length=20, verbose_name='市')
    district = models.CharField(blank=True,null=True, max_length=30, verbose_name='区')
    address = models.CharField(blank=True,null=True, max_length=100, verbose_name='详细地址')
    park_type = models.CharField(max_length=20,choices=PARK_TYPE,default = '住宅',verbose_name='停车场类型')
    property = models.CharField(blank=True,null=True, max_length=50, verbose_name='物业公司')
    Property_contact = models.CharField(blank=True,null=True, max_length=50, verbose_name='停车场联系人')
    Property_tele = models.CharField(blank=True, null=True, max_length=50, verbose_name='联系人电话')
    space_number = models.CharField(blank=True, null=True, max_length=10,verbose_name='车位数')
    carriage_way =models.CharField(blank=True, null=True, max_length=50, verbose_name='进出口数量')
    director = models.ForeignKey(Employee, on_delete=models.CASCADE,verbose_name='区域负责人')
    construction_time = models.DateTimeField(blank=True, null=True,verbose_name='施工时间', default=timezone.now)
    using_time = models.DateTimeField(blank=True, null=True, verbose_name='启用时间', default=timezone.now)
    watch_man = models.CharField(blank=True, null=True, max_length=20, verbose_name='值守人')
    train_man = models.CharField(blank=True, null=True, max_length=20, verbose_name='培训人')
    remark = models.CharField(blank=True,null=True,max_length=200,verbose_name='备注')

    class Meta:
        ordering = ('park_id',)
        verbose_name = '停车场列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.park_id


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name