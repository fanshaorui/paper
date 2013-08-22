from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import changeProfileForm,ProfileForm
from .models import Profile

def register(request):
    	if request.method=="POST":
		form=ProfileForm(request.POST)
		if form.is_valid():
			clean_register=form.cleaned_data
			try:
				user=User.objects.create_user(username=clean_register['name'],password=clean_register['password'],email=clean_register['email'])
				user.save()
			except:
				print "user failed"
			try:
				profile=Profile(user=user,phonenumber=clean_register['phonenumber'])
				profile.save()
			except:
				print "profile failed"
			auth.logout(request)
			try:
			    user_login=auth.authenticate(username=clean_register['name'],password=clean_register['password'])
			    if user_login is not None:
				auth.login(request,user_login)
				request.session['userkind']="customer"
				return HttpResponseRedirect(reverse("require.views.newRequirement"))
			    return render_to_response("customer/register.html",RequestContext(request,dict(form=form)))
			except:
			    render_to_response("customer/register.html",RequestContext(request,dict(form=form)))
		else:
		    print form.errors
		    return render_to_response("customer/register.html",RequestContext(request,dict(form=form)))
        else:
            return render_to_response("customer/register.html",RequestContext(request,dict(form=ProfileForm())))
@login_required
def profilePage(request):
    if request.method=="POST":
	form=changeProfileForm(request.POST)
	if form.is_valid():
	    newform=form.cleaned_data
	    try:
		newuser=User.objects.get(username=request.user.username)
		newuser.set_password(newform['password'])
		newuser.email=newform['email']
		newuser.save()
	    except:
		print "user info change error"
		HttpResponseRedirect("/")
	    try:
		newprofile=Profile.objects.get(user=request.user)
		newprofile.phonenumber=newform['phonenumber']
		newprofile.save()
		auth.logout(request)
		user_login=auth.authenticate(username=newuser.username,password=newform['password'])
		auth.login(request,user_login)
		request.session['userkind']='customer'
	    except:
		print "needprofile change error"
		return HttpResponseRedirect('/')
            return HttpResponseRedirect(reverse("customer.views.profilePage"))
        else:
            return render_to_response("customer/profile.html",RequestContext(request,dict(form=form)))   
    elif request.session['userkind']=="customer":
	return render_to_response("customer/profile.html",RequestContext(request,dict(form=changeProfileForm())))
    else:
	return HttpResponseRedirect("/")