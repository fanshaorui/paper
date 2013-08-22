# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
import main,require,transaction,writer,customer
admin.autodiscover()

urlpatterns = patterns('',
#admin.app
    url(r'^admin/', include(admin.site.urls)),
#customer.app
    url(r'^customer/profile/$','customer.views.profilePage'),#需求方个人资料修改页面
    url(r'^accounts/register/require/$','customer.views.register'),#需求方注册页
    url(r'^accounts/register/require/submit/$','customer.views.registerSubmit'),#需求方提交注册表单
    url(r'^accounts/register/require/change/submit/$','customer.views.profileChangeSubmit'),#需求方修改个人资料表单
#writer.app
    url(r'^writer/profile/edit/$','writer.views.profilePage'),#作者个人资料修改页面
    url(r'^accounts/register/writer/$','writer.views.register'),#作者注册
    url(r'^accounts/register/writer/submit/$','writer.views.registerSubmit'),#作者提交注册表单
    url(r'^accounts/register/writer/change/submit/$','writer.views.registerChangeSubmit'),#作者修改个人资料表单
    url(r'^writer/profile/(\d+)/$','writer.views.writerprofile'),#作者个人信息展示页
#require.app
    url(r'^require/new/$','require.views.newRequirement'),#需求方提交新需求页面
    url(r'^require/new/submit/$','require.views.newRequirementSubmit'),#需求方提交新需求表单 
    url(r'^customer/market/$','require.views.customerRequirementMarket'),#需求方查看全站需求列表
    url(r'^writer/market/$','require.views.writerRequirementMarket'),#写手查看全站需求列表
    url(r'^require/detail/(\d+)/$','require.views.detail'),#需求细节展示页
    url(r'^bid/(\d+)/$','require.views.bid'),#竞标
    url(r'^writer/bidlist/$','require.views.writerBidList'),#作者参与竞标列表
    url(r'^customer/requirelist/$','require.views.customerRequirmentList'),#需求方需求列表
#transaction.app
    url(r'^writer/transaction/$','transaction.views.writerTransactionList'),#写手交易列表
    url(r'^customer/transaction/$','transaction.views.customerTransactionList'),#需求方交易列表
    url(r'^transaction/(\d+)/$','transaction.views.TransactionDetail'),#单条交易详情页
    url(r'^requirement/submitBid/$','transaction.views.submitBid'),#提交竞标
    url(r'^finishtransaction/(\d+)$','transaction.views.finishTransaction'),#论文已经发表，交易结束
#main.app
    url(r'^accounts/logout/$','main.views.logout_view'),#退出
    url(r'^accounts/loginform/$','main.views.login_form'),#登陆
    url(r'^about/$','main.views.about'),#关于页
    url(r'^$','main.views.main'),#首页
)

