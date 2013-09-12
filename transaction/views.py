# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Transaction
from require.models import Requirement
from django.core.mail import send_mail
from paper import mail
from alipay.alipay import *
from django.views.decorators.csrf import csrf_exempt
@login_required
def TransactionDetail(request,pk):
	transaction=Transaction.objects.get(pk=pk)
	if request.session['userkind']=="writer":
		if request.user==transaction.biduser:
			return render_to_response("writer/transactiondetail.html",RequestContext(request,dict(transaction=transaction)))
		else:
			return HttpResponseRedirect('/')
	elif request.session['userkind']=="customer":
		if request.user==transaction.requirementuser:
			return render_to_response("customer/transactiondetail.html",RequestContext(request,dict(transaction=transaction)))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
@login_required
def finishTransaction(request,pk):
	transaction=Transaction.objects.get(pk=pk)
	if transaction.requirementuser==request.user:
		if request.method=="POST":
			if request.POST["submit"]=="yes":
				transaction.finish=True
				transaction.save()
                                mail.sendmailthread('需求方已经确认论文发表','需求方已经确认论文发表，剩余80%款项我们会在3个工作日内打到您的银行账户上，请确认您的银行信息正确并注意查收','85lunwen@gmail.com', [transaction.biduser.email]).start()
				return HttpResponseRedirect(reverse("transaction.views.customerTransactionList"))
		else:
			return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")
@login_required
def submitBid(request):
	if request.method=="POST":
		requirement=Requirement.objects.get(pk=request.POST['requirement'])
		biduser=User.objects.get(pk=request.POST['biduser'])
                requirement.finish=True
                requirement.save()
                transaction=Transaction(requirementuser=request.user,biduser=biduser,requirement=requirement)
                transaction.save_order()
                url=create_direct_pay_by_user(transaction.order_id,u"帮我论文-论文支付款",requirement.theme,requirement.prize)
		return HttpResponseRedirect(url)
@login_required
def continuePay(request):
    if request.method=="POST":
        transaction=Transaction.objects.get(pk=request.POST['transaction'])
        requirement=transaction.requirement
        if transaction.pay==False:
            url=create_direct_pay_by_user(transaction.order_id,u"帮我论文-论文支付款",requirement.theme,requirement.prize)
            return HttpResponseRedirect(url)
    else:
        return HttpResponse("fail")

@login_required
def writerTransactionList(request):
	if request.session['userkind']=="writer":
		tlist=Transaction.objects.filter(biduser=request.user)
                #print tlist
		return render_to_response("writer/TransactionList.html",RequestContext(request,dict(tlist=tlist)))
@login_required
def customerTransactionList(request):
	if request.session['userkind']=="customer":
		tlist=Transaction.objects.filter(requirementuser=request.user)
		return render_to_response("customer/TransactionList.html",RequestContext(request,dict(tlist=tlist)))
@csrf_exempt
def notify_url_handler(request):
    if request.method == 'POST':
        if notify_verify(request.POST):
            print "return ok"
            tn = request.POST.get('out_trade_no')
            transaction=Transaction.objects.get(order_id=tn)
            transaction.pay=True
	    transaction.save()
            mail.sendmailthread('您中标了','您参与的竞标中标了,请登录85lunwen.com查看详情','85lunwen@gmail.com', [biduser.email]).start()
            return HttpResponse("success")
        else:
            return HttpResponse("fail")
    else:
        return HttpResponse("fail")
def return_url_handler(request):
    if notify_verify(request.GET):
        return HttpResponseRedirect(reverse('payment_success'))
    return HttpResponseRedirect(reverse('payment_error'))