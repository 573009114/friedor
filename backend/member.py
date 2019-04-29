# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
import random
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
        MemberForm(name=name,tel=tel,address=address,vipid=vipid).post_member()
        msg=HttpResponse('<script type="text/javascript">alert("保存成功");location.href="/member/"</script>')
        return msg    
    return render(req,'backend/member-add.htm',{'response':vipid}) 

def member_modify(req):
    '''修改会员信息'''
    return HttpResponse('123')

def member_delete(req):
    '''删除会员'''
    id=req.GET.get('id')
    response=MemberForm(id=id).delete_member()
    return HttpResponse('<script type="text/javascript">alert("记录删除成功");location.href="/member/"</script>')


def income(req):
    return render(req,'backend/income-list.htm')


def income_creat(req):
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