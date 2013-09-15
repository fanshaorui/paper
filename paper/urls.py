# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
import main,require,transaction,writer,customer,captcha
from django.views.generic import TemplateView
from django.contrib.sitemaps import GenericSitemap
from require.models import Requirement
import django_messages
admin.autodiscover()
require_dict = {
    'queryset': Requirement.objects.all(),
    'date_field': 'createdtime',
}
sitemaps = {
    # 'flatpages': FlatPageSitemap,
    'require': GenericSitemap(require_dict, priority=0.6),
}
urlpatterns = patterns('',
#admin.app
    url(r'^admin/', include(admin.site.urls)),
#customer.app
    url(r'^customer/profile/$','customer.views.profilePage'),#需求方个人资料修改页面
    url(r'^accounts/register/require/$','customer.views.register'),#需求方注册页
#writer.app
    url(r'^writer/profile/edit/$','writer.views.profilePage'),#作者个人资料修改页面
    url(r'^accounts/register/writer/$','writer.views.register'),#作者注册
    url(r'^writer/profile/(\d+)/$','writer.views.writerprofile'),#作者个人信息展示页
#require.app
    url(r'^require/new/$','require.views.newRequirement'),#需求方提交新需求页面
    url(r'^customer/market/$','require.views.customerRequirementMarket'),#需求方查看全站需求列表
    url(r'^writer/market/$','require.views.writerRequirementMarket'),#写手查看全站需求列表
    url(r'^require/detail/(\d+)/$','require.views.detail'),#需求细节展示页
    url(r'^bid/(\d+)/$','require.views.bid'),#竞标
    url(r'^writer/bidlist/$','require.views.writerBidList'),#作者参与竞标列表
    url(r'^customer/requirelist/$','require.views.customerRequirmentList'),#需求方需求列表
    url(r'require/delete/(\d+)/$','require.views.deleteMyRequire'),#删除发的需求
    url(r'require/edit/(\d+)/$','require.views.editMyRequire'),#修改发的需求
#transaction.app
    url(r'^writer/transaction/$','transaction.views.writerTransactionList'),#写手交易列表
    url(r'^customer/transaction/$','transaction.views.customerTransactionList'),#需求方交易列表
    url(r'^transaction/(\d+)/$','transaction.views.TransactionDetail'),#单条交易详情页
    url(r'^requirement/submitBid/$','transaction.views.submitBid'),#提交竞标
    url(r'^transaction/notify_url/$','transaction.views.notify_url_handler'),#通知回调
    url(r'^transaction/return_url/$','transaction.views.return_url_handler'),#跳转回调
    url(r'^transaction/payment_success/$',TemplateView.as_view(template_name="transaction/success.html"), name="payment_success"),#成功跳转
    url(r'^transaction/payment_error/$',TemplateView.as_view(template_name="transaction/error.html"), name="payment_error"),#失败跳转
    url(r'^finishtransaction/(\d+)$','transaction.views.finishTransaction'),#论文已经发表，交易结束
    url(r'^transaction/continuepay/$','transaction.views.continuePay'),#对已经提交但是未完成付款的订单继续付款
#main.app
    url(r'^accounts/logout/$','main.views.logout_view'),#退出
    url(r'^accounts/login/$','main.views.loginpage'),#登陆页
    url(r'^about/$','main.views.about'),#关于页
    url(r'^market/$','main.views.market'),#匿名访问论文需求市场
    url(r'^detail/(\d+)/$','main.views.detail'),#匿名访问论文需求详情页
    url(r'^writerindex/$','main.views.writerindex'),#我会写论文
    url(r'^$','main.views.main'),#我想发论文
    url(r'^captcha/', include('captcha.urls')),#验证码
#messages
    url(r'^messages/', include('django_messages.urls')),#messages
#sitemap
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)


