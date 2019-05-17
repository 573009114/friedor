# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Members(models.Model):
    name=models.CharField(max_length=50, verbose_name="姓名", default="")
    mobel=models.CharField(max_length=11, verbose_name="手机号", default="")
    address=models.CharField(max_length=50, verbose_name="地址", default="")
    secret=models.CharField(max_length=16, verbose_name="密钥", default="")

    class Meta():
        db_table= 'friedor_members'

class Income(models.Model):
    amount=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="金额")
    mealname=models.ForeignKey('FoodProducts')
    date=models.DateTimeField('日期',default = timezone.now)
    class Meta():
        db_table= 'friedor_incomes'

class Expenditure(models.Model):
    amount=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="金额")
    dishname=models.ForeignKey('Stock')
    date=models.DateTimeField('日期',default = timezone.now)

    class Meta():
        db_table= 'friedor_expenditures'

class FoodProducts(models.Model):
    mealname=models.CharField(max_length=50, verbose_name="餐品名", default="")
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="定价")
 
    class Meta():
        db_table= 'friedor_foodproducts'

class Stock(models.Model):
    typed=models.CharField(max_length=50, verbose_name="品类", default="")
    dishname=models.CharField(max_length=50, verbose_name="食材名", default="")
    number=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="单价")
    total_price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="总价")

    class Meta():
        db_table= 'friedor_stocks'

class Search(models.Model):
    mobel=models.ForeignKey('Members')
    class Meta():
        db_table= 'friedor_search'


class User(models.Model):
    STATUS = (
              (0,'超级管理员'),
              (1,'普通用户'),             
              )
    ACTIVE = (
              (0,'已激活'),
              (1,'未激活')
        )
    username=models.CharField('用户名',max_length=50, default="")
    password=models.CharField('密码',max_length=50,default="")
    email=models.EmailField('邮箱',max_length=50)
    is_superuser=models.IntegerField(choices=STATUS,default='')
    is_active=models.IntegerField(choices=ACTIVE,default='')
    class Meta():
        db_table= 'friedor_user'

class Role(models.Model):
    role_name=models.CharField('角色名',max_length=50, default="")
    class Meta():
        db_table= 'friedor_role'

class Menu(models.Model):
    menu_name=models.CharField('权限菜单名',max_length=50, default="")
    main_id=models.IntegerField('父级ID',max_length=5)
    main_url=models.CharField('连接路径',max_length=50, default="")
    class Meta():
        db_table= 'friedor_menu'

class UserRole(models.Model): 
    user_id=models.ForeignKey('User')
    role_id=models.ForeignKey('Role')
    class Meta():
        db_table= 'friedor_userrole'

class UserMenu(models.Model): 
    user_id=models.ForeignKey('User')
    main_id=models.ForeignKey('Menu')
    menudom=models.IntegerField(max_length=5)
    class Meta():
        db_table= 'friedor_usermenu'

    