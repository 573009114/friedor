# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from backend import *

# Create your views here.
def member_list(req):
    return render(req,'backend/member-list.htm') 

def member_creat(req):
    return render(req,'backend/member-add.htm') 

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