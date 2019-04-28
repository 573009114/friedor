# -*- coding: utf-8 -*-
"""friedor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from backend import index,account,member

urlpatterns = [
    url(r'^index/$',index.index,name='index'),
    # 会员管理路由
    url(r'^member/$',member.member_list,name='list'),
    url(r'^member/create',member.member_creat,name='creat'),
    # 收入路由
    url(r'^income/$',member.income,name='income'),
    url(r'^income/create',member.income_creat,name='incomecreat'),
    # 支出路由
    url(r'^expenditure/$',member.expenditure,name='expenditure'),
    url(r'^expenditure/create',member.expenditure_creat,name='expenditurecreat'),
    # 食材路由
    url(r'^fooding/$',member.fooding,name='fooding'),
    url(r'^fooding/create',member.fooding_creat,name='foodingcreat'),
    # 库存路由
    url(r'^stock/$',member.stock,name='stock'),
    url(r'^stock/create',member.stock_creat,name='stockcreat'),
    # 登录路由
    url(r'^login/$',account.login,name='login'),
    url(r'^logout/$',account.logout,name='logout'),
    url(r'^channgepwd/$',account.channgePwd,name='channgepwd'),
]
