from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import changeProfileForm,ProfileForm
def register(request):
    	if request.method=="POST":
		form=ProfileForm(request.POST)
		if form.is_valid():
                        human=True
			clean_register=form.cleaned_data
			try:
				user=User.objects.create_user(username=clean_register['name'],password=clean_register['password'],email=clean_register['email'])
				user.save()	
			except:
				print "user failed"
				return render_to_response("writer/register.html",RequestContext(request,dict(form=form)))
			try:
				profile=Profile(user=user,phonenumber=clean_register['phonenumber'],realname=clean_register['realname'],selfdescription=clean_register['selfdescription'],bankaccount=clean_register['bankaccount'],bank=clean_register['bank'])
				profile.save()
			except:
				print "profile failed"
				render_to_response("writer/register.html",RequestContext(request,dict(form=form)))
			auth.logout(request)
			try:
				user_login=auth.authenticate(username=clean_register['name'],password=clean_register['password'])
				if user_login is not None:
					auth.login(request,user_login)
					request.session['userkind']="writer"
					return HttpResponseRedirect(reverse("require.views.writerRequirementMarket"))
				render_to_response("writer/register.html",RequestContext(request,dict(form=form)))
			except:
				print "auth failed"
				render_to_response("writer/register.html",RequestContext(request,dict(form=form)))
		else:
			print form.errors
			return render_to_response("writer/register.html",RequestContext(request,dict(form=form)))
        else:
            return render_to_response("writer/register.html",RequestContext(request,dict(form=ProfileForm())))

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
		return render_to_response("writer/profilepage.html",RequestContext(request,dict(form=form)))
	    try:
		newprofile=Profile.objects.get(user=request.user)
		newprofile.phonenumber=newform['phonenumber']
		newprofile.realname=newform['realname']
		newprofile.selfdescription=newform['selfdescription']
                newprofile.bank=newform['bank']
                newprofile.bankaccount=newform['bankaccount']
		newprofile.save()
		auth.logout(request)
		user_login=auth.authenticate(username=newuser.username,password=newform['password'])
		auth.login(request,user_login)
		request.session['userkind']='writer'
	    except:
		print "needprofile change error"
		HttpResponseRedirect('/')
            return HttpResponseRedirect(reverse("writer.views.profilePage"))
        else:
            return render_to_response("writer/profilepage.html",RequestContext(request,dict(form=form)))
    elif request.session['userkind']=="writer":
        profile=Profile.objects.get(user=request.user)
        print profile.phonenumber
        form=changeProfileForm(initial={'email':request.user.email,'phonenumber':profile.phonenumber,'realname':profile.realname,'selfdescription':profile.selfdescription,'bankaccount':profile.bankaccount,'bank':profile.bank})
	return render_to_response("writer/profilepage.html",RequestContext(request,dict(form=form)))
    else:
	return HttpResponseRedirect("/")
@login_required
def writerprofile(request,pk):
	if request.session['userkind']=="customer":
		writer=User.objects.get(pk=pk)
		writerprofile=Profile.objects.get(user=writer)
		preurl=request.META.get('HTTP_REFERER',"/")
		return render_to_response("writer/profile.html",dict(writerprofile=writerprofile,preurl=preurl))

