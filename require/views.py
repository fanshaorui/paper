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
@login_required
def customerRequirmentList(request):
	lists=Requirement.objects.filter(creator=request.user,finish=False)
	return render_to_response("customer/requirementlist.html",dict(lists=lists))
@login_required
def newRequirement(request):
	return render_to_response("customer/newrequirement.html",RequestContext(request,dict(form=RequirementForm())))
@login_required
def customerRequirementMarket(request):
	if request.session['userkind']=="customer":
	    lists=Requirement.objects.filter(finish=False)
	    return render_to_response("customer/market.html",dict(lists=lists))
	else:
	    return HttpResponseRedirect("/")
#writer user
@login_required
def writerRequirementMarket(request):
	if request.session['userkind']=="writer":
		lists=Requirement.objects.filter(finish=False)
		return render_to_response("writer/market.html",dict(lists=lists))
	else:
		return HttpResponseRedirect("/")
@login_required		
def bid(request,pk):
	if request.method=="POST":
		if request.POST['submit']=='yes':
			requirement=Requirement.objects.get(pk=pk)
			requirement.biduser.add(request.user)
			requirement.save()
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
			if request.user in requirement.biduser.all():
				didbid=True
			else:
				didbid=False
			return render_to_response("writer/detail.html",RequestContext(request,dict(requirement=requirement,didbid=didbid)))
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
def newRequirementSubmit(request):
	if request.method=="POST":
		form=RequirementForm(request.POST)
		if form.is_valid():
			requirementform=form.cleaned_data
			try:
				requirement=Requirement(creator=request.user,description=requirementform['description'],scifactor=requirementform['scifactor'],prize=requirementform['prize'])
				requirement.save()
				return HttpResponseRedirect("/")
			except:
				print "save failed"
				return HttpResponseRedirect("/")
		else:
			print form.errors
			return HttpResponseRedirect("/")
	return HttpResponseRedirect("/")