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


    