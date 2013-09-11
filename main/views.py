# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import LoginForm
from require.models import Requirement
import customer,writer,cms
# Create your views here.
def main(request):
	if request.user.is_authenticated():
	    if request.session['userkind']=="customer":
		return HttpResponseRedirect(reverse("require.views.newRequirement"))
	    elif request.session['userkind']=="writer":
		return HttpResponseRedirect(reverse("writer.views.profilePage"))
	else:
            #wlist=cms.models.writerExample.objects.all()
            #clist=cms.models.customerExample.objects.all()
	    return render_to_response("index.html",RequestContext(request,dict()))
#logout page
def logout_view(request):
	auth.logout(request)
	#del request.session['userkind']
	return HttpResponseRedirect("/")
#about
def about(request):
	return render_to_response("about.html",dict())
def loginpage(request):
        if request.user.is_authenticated():
	    if request.session['userkind']=="customer":
		return HttpResponseRedirect(reverse("require.views.newRequirement"))
	    elif request.session['userkind']=="writer":
		return HttpResponseRedirect(reverse("writer.views.profilePage"))
	elif request.method=="POST":
            wlist=cms.models.writerExample.objects.all()
            clist=cms.models.customerExample.objects.all()
	    form=LoginForm(request.POST)
	    if form.is_valid():
                logininfo=form.cleaned_data
		username=logininfo["name"]
		password=logininfo["password"]
		try:
		    user=auth.authenticate(username=username,password=password)
                    print user
		    if user is not None:
                        auth.login(request, user)
			try:
                            customer.models.Profile.objects.get(user=user)
                            request.session['userkind']="customer"
			    print request.session['userkind']
			    return HttpResponseRedirect(reverse("require.views.newRequirement"))
			except customer.models.Profile.DoesNotExist:
                            print "not a customer"
                            try:
                                writer.models.Profile.objects.get(user=user)
                                request.session['userkind']="writer"
                                print request.session['userkind']
                                return HttpResponseRedirect(reverse("require.views.writerRequirementMarket"))
                            except writer.models.Profile.DoesNotExist:
                                print "not a writer also?"
                                return render_to_response("login.html",RequestContext(request,dict(form=form,wlist=wlist,clist=clist)))
		    else:
			message="密码错误或者用户名不存在"
			return render_to_response("login.html",RequestContext(request,dict(form=form,message=message,wlist=wlist,clist=clist)))
		except:
		    message="密码错误或者用户名不存在"
		    return render_to_response("login.html",RequestContext(request,dict(form=form,message=message,wlist=wlist,clist=clist)))
	    else:
                return render_to_response("login.html",RequestContext(request,dict(form=form,wlist=wlist,clist=clist)))
        else:
            wlist=cms.models.writerExample.objects.all()
            clist=cms.models.customerExample.objects.all()
            return render_to_response("login.html",RequestContext(request,dict(form=LoginForm(),wlist=wlist,clist=clist)))
def writerindex(request):

	if request.user.is_authenticated():
	    if request.session['userkind']=="customer":
		return HttpResponseRedirect(reverse("require.views.newRequirement"))
	    elif request.session['userkind']=="writer":
		return HttpResponseRedirect(reverse("writer.views.profilePage"))
	else:
            #wlist=cms.models.writerExample.objects.all()
            #clist=cms.models.customerExample.objects.all()
	    return render_to_response("writerindex.html",RequestContext(request,dict()))
def market(request):
    lists=Requirement.objects.filter(finish=False).order_by("-createdtime")
    return render_to_response("market.html",dict(lists=lists),context_instance=RequestContext(request))
def detail(request,pk):
    requirement=Requirement.objects.get(pk=pk)
    return render_to_response("detail.html",RequestContext(request,dict(requirement=requirement)))
