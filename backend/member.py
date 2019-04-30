# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
import random
import time
from backend import *
from querydb import *

# Create your views here.
def member_list(req):
    '''获取会员列表'''
    data=MemberForm().view_member_list()
    return render(req,'backend/member-list.htm',{'data':data}) 

def member_creat(req):
    '''初始化会员值'''
    name=req.POST.get('name')
    tel=req.POST.get('tel')
    address=req.POST.get('address')
    vipid=random.randint(100000000000000,999999999999999)
    
    if req.method == 'POST':
        if len(tel) >0 and len(name)>0:
            MemberForm(name=name,tel=tel,address=address,vipid=vipid).post_member()
            msg="保存成功"
        else:
            msg="姓名或者电话不能为空"
        return HttpResponse('<script type="text/javascript">alert("%s");location.href="/member/"</script>' %msg)    
    return render(req,'backend/member-add.htm',{'response':vipid}) 

def member_modify(req):
    '''修改会员信息'''
    return HttpResponse('123')

def member_delete(req):
    '''删除会员'''
    id=req.GET.get('id')
    try:
        response=MemberForm(id=id).delete_member()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


def income(req):
    time=time.strftime("%Y-%m-%d", time.localtime())
    return render(req,'backend/income-list.htm')


def income_creat(req):
    '''初始化收入配置'''

    return render(req,'backend/income-add.htm')


def expenditure(req):
    return render(req,'backend/expenditure-list.htm')

def expenditure_creat(req):
    return render(req,'backend/expenditure-add.htm')

def fooding(req):
    return render(req,'backend/fooding-list.htm')

def fooding_creat(req):
    return render(req,'backend/fooding-add.htm')

def stock(req):
    return render(req,'backend/stock-list.htm')

def stock_creat(req):
    return render(req,'backend/stock-add.htm')