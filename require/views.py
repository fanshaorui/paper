# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Requirement
from .forms import RequirementForm
import customer
from django.core.mail import send_mail
from paper import mail
@login_required
def customerRequirmentList(request):
	lists=Requirement.objects.filter(creator=request.user,finish=False).order_by("-createdtime")
	return render_to_response("customer/requirementlist.html",dict(lists=lists))
@login_required
def newRequirement(request):
    if request.method=="POST":
	form=RequirementForm(request.POST)
	if form.is_valid():
	    requirementform=form.cleaned_data
	    try:
		requirement=Requirement(creator=request.user,description=requirementform['description'],scifactor=requirementform['scifactor'],prize=requirementform['prize'],theme=requirementform['theme'],circle_min=requirementform['circle_min'],circle_max=requirementform['circle_max'])
		requirement.save()
		return HttpResponseRedirect(reverse("require.views.customerRequirmentList"))
	    except:
		print "save failed"
		return HttpResponseRedirect("/")
	else:
            return render_to_response("customer/newrequirement.html",RequestContext(request,dict(form=form)))
    else:
	return render_to_response("customer/newrequirement.html",RequestContext(request,dict(form=RequirementForm())))
@login_required
def customerRequirementMarket(request):
	if request.session['userkind']=="customer":
	    lists=Requirement.objects.filter(finish=False).order_by("-createdtime")
	    return render_to_response("customer/market.html",dict(lists=lists),context_instance=RequestContext(request))
	else:
	    return HttpResponseRedirect("/")
#writer user
@login_required
def writerRequirementMarket(request):
	if request.session['userkind']=="writer":
		lists=Requirement.objects.filter(finish=False).order_by("-createdtime")
		return render_to_response("writer/market.html",dict(lists=lists),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")
@login_required		
def bid(request,pk):
	if request.method=="POST":
		if request.POST['submit']=='yes':
			requirement=Requirement.objects.get(pk=pk)
			requirement.biduser.add(request.user)
			requirement.save()
                        if requirement.biduser.all().count()==1:
                            print "yes"+requirement.creator.email
                            mail.sendmailthread('有人竞标您的需求','有人竞标您的需求,请登录85lunwen.com查看详情','85lunwen@gmail.com', [requirement.creator.email]).start()
			return HttpResponseRedirect(reverse("require.views.detail",args=[pk]))
		elif request.POST['submit']=='no':
			requirement=Requirement.objects.get(pk=pk)
			requirement.biduser.remove(request.user)
			requirement.save()
			return HttpResponseRedirect(reverse("require.views.detail",args=[pk]))
@login_required
def detail(request,pk):
	requirement=Requirement.objects.get(pk=pk)
	if not requirement.finish:
		if request.session['userkind']=="customer":
			bidlist=[]
			if requirement.creator==request.user:
				bidlist=requirement.biduser.all()
			return render_to_response("customer/detail.html",RequestContext(request,dict(requirement=requirement,bidlist=bidlist)))
		elif request.session['userkind']=="writer":
                        profile=customer.models.Profile.objects.get(user=requirement.creator)
                        phonenumber=profile.phonenumber
			if request.user in requirement.biduser.all():
				didbid=True
			else:
				didbid=False
			return render_to_response("writer/detail.html",RequestContext(request,dict(requirement=requirement,didbid=didbid,phonenumber=phonenumber)))
	else:
		return HttpResponseRedirect('/')
@login_required
def writerBidList(request):
	user=request.user
	allRequirement=Requirement.objects.filter(finish=False)
	userbid=[]
	for requirement in allRequirement:
		if user in requirement.biduser.all():
			userbid.append(requirement)
	return render_to_response("writer/mybid.html",dict(userbid=userbid))
@login_required
def deleteMyRequire(request,pk):
    requirement=Requirement.objects.get(pk=pk)
    if requirement.creator==request.user:
        requirement.delete()
        return HttpResponseRedirect(reverse("require.views.customerRequirmentList"))
    else:
        HttpResponseRedirect(reverse("/"))

