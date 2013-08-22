from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Transaction
from require.models import Requirement
@login_required
def TransactionDetail(request,pk):
	transaction=Transaction.objects.get(pk=pk)
	if request.session['userkind']=="writer":
		if request.user==transaction.biduser:
			return render_to_response("writer/transactiondetail.html",dict(transaction=transaction))
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
		transaction.save()
		return HttpResponseRedirect("/")
@login_required
def writerTransactionList(request):
	if request.session['userkind']=="writer":
		tlist=Transaction.objects.filter(biduser=request.user)
		return render_to_response("writer/TransactionList.html",dict(tlist=tlist))
@login_required
def customerTransactionList(request):
	if request.session['userkind']=="customer":
		tlist=Transaction.objects.filter(requirementuser=request.user)
		return render_to_response("customer/TransactionList.html",dict(tlist=tlist))
