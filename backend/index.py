# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def index(req):
    return render(req,'backend/index.html') 

